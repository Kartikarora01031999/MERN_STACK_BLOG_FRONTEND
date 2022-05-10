import json
import re
from urllib.request import DataHandler
from flask import Flask, request, jsonify, redirect, session, make_response, render_template, url_for
from flask_session import Session
from flask_mongoengine import MongoEngine
import cloudinary
import cloudinary.uploader
import pymongo
from models import *
from pymongo import MongoClient, ReturnDocument
import urllib
from bson.json_util import dumps,loads
from helpers import *
''' firebase modules '''
import os
import firebase_admin
from firebase_admin import credentials,auth
from firebase import Firebase
import traceback
import uuid
import datetime
import asyncio
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition)
import mongoengine as me
from bson.objectid import ObjectId
from flask_cors import CORS
from dotenv import load_dotenv
import razorpay
client = razorpay.Client(auth=(os.getenv('RAZORPAY_APP_ID'),os.getenv('RAZORPAY_APP_SECRET')))
cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred)
app = Flask(__name__, template_folder='templates',static_folder='static')
app.secret_key = "abc"
app.config['MONGODB_SETTINGS'] = {
    'host': "mongodb+srv://kartik:Kartik_01@cluster0.fvxsb.mongodb.net/EcomDataBase?retryWrites=true&w=majority",
}
CORS(app)
CORS(app)
db = MongoEngine()
db.init_app(app)
cluster=MongoClient("mongodb+srv://kartik:Kartik_01@cluster0.fvxsb.mongodb.net/EcomDataBase?retryWrites=true&w=majority")

ecom_db = cluster["EcomDataBase"]
load_dotenv()
firebaseConfig =json.load(open('./fbconfig.json'))


print(firebaseConfig)
pb = Firebase(firebaseConfig)

sendgrid_api_key = os.getenv('SENDGRID_API_KEY')

users = ecom_db["user"]
jewellery_boxes = ecom_db["jewellery_box"]
jewellery_bages = ecom_db["jewellery_bag"]
carts = ecom_db["cart"]


#Wrap check token
def check_token(f):
    '''
    Middle Ware to check Auth Token

    '''

    def wrap(*args,**kwargs):
        print(request.headers)
        print(request.headers.get('authorization'))
        if not request.headers.get('authorization'):
            return {'message': 'No token provided'},400
        try:
            user = auth.verify_id_token(request.headers['authorization'])
            request.user = user
        except:
            return {'message':'Invalid token provided.'},400
        return f(*args, **kwargs)
    wrap.__name__=f.__name__
    return wrap


#create or update user
@app.route("/api/create-update-user", methods=["POST"])
@check_token
def create_update_user():
    '''
    Function to Create or Update User

    '''
    print(request.user)
    email=request.user["email"]
    user=users.find_one_and_update({"email": email},{"$set":{"email":email}}, return_document=ReturnDocument.AFTER)
    if user:
        return jsonify(user),200
    else:
        doc={'_id': uuid.uuid4().hex,
        'name': "",
        'email':email,
        'phone_number':"",
        'role':'user',
        "business_name":"",
        "gst_in":"",
        "cart":"",
        "address":""
        }
        user=users.insert_one(doc)
        return jsonify({
        "_id": user.inserted_id,
        "email": email,
        "role":"user"
        }),200



#current user
@app.route("/api/current-user", methods=["POST"])
@check_token
def current_user():
    '''
    Api to fetch Current User 

    '''
    current_user =json.loads(dumps(users.find_one({'email': request.user["email"]}))) 
    if current_user:
        return jsonify({"data": current_user}),200
    else:
        return jsonify({"error":"Invalid User"}),401

#sending contact query mail
@app.route('/api/contact-us', methods= ["POST"])
def contact_us():
    '''
    Api to Send mail for contact query

    '''

    reciever_name = request.json.get('name') or ""
    reciever_email = request.json.get('email') or ""
    print(reciever_email)
    reciever_phone = request.json.get("phone") or ""
    reciever_message = request.json.get("message") or ""
    message= Mail(from_email="vp@kavaratech.com",
                    to_emails="kartikarora1399@gmail.com",
                    subject= "Query From "+reciever_name,
                    html_content= "<strong>"+"Contact Email is : "+reciever_email+"</strong><br><br>\
                    <strong>"+"Contact phone no. is : "+reciever_phone+"</strong><br><br>\
                    <p>"+reciever_message +"</p>")
    try:
        sg=SendGridAPIClient(sendgrid_api_key)
        response=sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
        return jsonify({"success":"Mail sent Succeessfully"}),200
    except Exception:
        return jsonify({"error":"Unable to contact"}),404

'''
jewellery_box API KEYS
---------------------------------------------------------------------------------------------------------------------------------------------
'''
@app.route('/api/admin/create-jewellery-box', methods= ["POST"])
@check_token
def create_jewellery_box():
    '''
    Admin to Create jewellery-box
    '''
    print(request.user["email"])
    user =User.objects(email=request.user["email"]).first()
    print(request.json)
    if user['role']=="admin":
        jewellery_box_items = request.json
        print(jewellery_box_items)
        try:
            jewellery_box = add_jewellery_box_helper(jewellery_box_items, "JewelleryBox")
            jewellery_box.save()
        except Exception as e:
            return jsonify({"error": str(e)[:100]}),400
        return jsonify({"data": jewellery_box, "message": "jewellery_box Created"})
    else:
        return jsonify({"message": "Unauthorized User"}),403

@app.route("/api/admin/delete-jewellery-box", methods=["POST"])
@check_token
def delete_jewellery_box():
    '''
    Admin to Delete jewellery-box
    '''
    user =User.objects(email=request.user['email']).first()
    if user['role']=="admin":
        try:
            jewellery_box = JewelleryBox.objects(id =request.json["_id"] ).first()
            print(jewellery_box.id)
            jewellery_box.delete()
            return jsonify({"message": "jewellery_box Deleted"}),204
        except:
            return jsonify({"error":"jewellery_box Not Found"}),404
        
    else:
        return jsonify({"message": "Unauthorized User"}),403

@app.route("/api/admin/get-jewellery-boxes", methods=["POST","GET"])
#@check_token
def get_all_jewellery_boxes():
    '''
    Admin Api to Fetch all jewellery-boxes

    '''
    hack= request.data
    try:
        page = request.json.get('page')
        total_count= request.json["total_count"]
        precount = total_count * (page-1)
        count= total_count *page
        jewellery_boxes=JewelleryBox.objects()[precount:count]
    except:
        print("contnue..")
        jewellery_boxes=JewelleryBox.objects()
    if jewellery_boxes:
        return jsonify({"jewellery_boxes": jewellery_boxes}),200
    else:
        return jsonify("No jewellery_boxes found"),200

@app.route("/api/get-jewellery-boxes-by-price", methods=["POST","GET"])
#@check_token
def get_all_jewellery_boxes_by_price():
    '''
    Admin Api to Fetch all jewellery-boxes

    '''
    hack= request.data
    try:
        page = request.json.get('page')
        total_count= request.json["total_count"]
        precount = total_count * (page-1)
        count= total_count *page
        if request.json["category"]=="":
            jewellery_boxes=JewelleryBox.objects()[precount:count]
        else:
            jewellery_boxes=JewelleryBox.objects(category=request.json["category"])[precount:count]
    except:
        print("contnue..")
        if request.json["category"]=="":
            jewellery_boxes=JewelleryBox.objects()
        else:
            jewellery_boxes=JewelleryBox.objects(category=request.json["category"])
    if jewellery_boxes:
        jewellery_boxes=[jewellery_box  for jewellery_box in jewellery_boxes if jewellery_box.price in range(request.json["min"], request.json["max"]+1)] 
    
        return jsonify({"jewellery_box": jewellery_boxes}),200
    else: return jsonify({"jewellery_boxes": []}),200

@app.route("/api/get-jewellery-boxes-by-category", methods=["POST","GET"])
#@check_token
def get_all_jewellery_boxes_by_category():
    '''
    Admin Api to Fetch all Normal jewellery_boxes by category
    '''
    hack= request.data
    try:
        page = request.json.get('page')
        total_count= request.json["total_count"]
        precount = total_count * (page-1)
        count= total_count *page
        jewellery_boxes=JewelleryBox.objects(category=request.json["category"])[precount:count]
    except:
        print("contnue..")
        jewellery_boxes=JewelleryBox.objects(category=request.json["category"]) 
    if jewellery_boxes:
        return jsonify({"jewellery_boxes": jewellery_boxes}),200
    else: return jsonify({"jewellery_boxes": []}),200



@app.route("/api/admin/update-jewellery-box", methods=["POST"])
@check_token
def update_jewellery_box():
    '''
    Admin Api to update jewellery-box

    '''
    user =User.objects(email=request.user['email']).first() 
    if user['role']=="admin":
        try: 
            jewellery_box_items=request.json
            try:
                app_jewellery_box=JewelleryBox.objects(id = request.json.get('_id')).first()
            except:
                return jsonify({"error":"jewellery_box Not Found"}),404
            jewellery_box = update_jewellery_box_helper(jewellery_box_items, app_jewellery_box)
            jewellery_box.save()
            return jsonify({"message":"jewellery_box Updated Successfully"}),200
        except Exception as e:
            return jsonify({"message": str(e)[:100]}),400      
    else:
        return jsonify({"message": "Unauthorized User"}),403

'''
jewellery_bag API KEYS
---------------------------------------------------------------------------------------------------------------------------------------------
'''
@app.route('/api/admin/create-jewellery-bag', methods= ["POST"])
@check_token
def create_jewellery_bag():
    '''
    Admin to Create jewellery-bag
    '''
    print(request.user["email"])
    user =User.objects(email=request.user["email"]).first()
    print(request.json)
    if user['role']=="admin":
        jewellery_bag_items = request.json
        print(jewellery_bag_items)
        try:
            jewellery_bag = add_jewellery_box_helper(jewellery_bag_items, "JewelleryBag")
            jewellery_bag.save()
        except Exception as e:
            return jsonify({"error": str(e)[:100]}),400
        return jsonify({"data": jewellery_bag, "message": "jewellery_bag Created"})
    else:
        return jsonify({"message": "Unauthorized User"}),403

@app.route("/api/admin/delete-jewellery-bag", methods=["POST"])
@check_token
def delete_jewellery_bag():
    '''
    Admin to Delete jewellery-bag
    '''
    user =User.objects(email=request.user['email']).first()
    if user['role']=="admin":
        try:
            jewellery_bag = JewelleryBag.objects(id =request.json["_id"] ).first()
            print(jewellery_bag.id)
            jewellery_bag.delete()
            return jsonify({"message": "jewellery_bag Deleted"}),204
        except:
            return jsonify({"error":"jewellery_bag Not Found"}),404
        
    else:
        return jsonify({"message": "Unauthorized User"}),403

@app.route("/api/admin/get-jewellery-bages", methods=["POST","GET"])
#@check_token
def get_all_jewellery_bages():
    '''
    Admin Api to Fetch all jewellery-bages

    '''
    hack= request.data
    try:
        page = request.json.get('page')
        total_count= request.json["total_count"]
        precount = total_count * (page-1)
        count= total_count *page
        jewellery_bages=JewelleryBag.objects()[precount:count]
    except:
        print("contnue..")
        jewellery_bages=JewelleryBag.objects()
    if jewellery_bages:
        return jsonify({"jewellery_bages": jewellery_bages}),200
    else:
        return jsonify("No jewellery_bages found"),200

@app.route("/api/get-jewellery-bages-by-price", methods=["POST","GET"])
#@check_token
def get_all_jewellery_bages_by_price():
    '''
    Admin Api to Fetch all jewellery-bages

    '''
    hack= request.data
    try:
        page = request.json.get('page')
        total_count= request.json["total_count"]
        precount = total_count * (page-1)
        count= total_count *page
        if request.json["category"]=="":
            jewellery_bages=JewelleryBag.objects()[precount:count]
        else:
            jewellery_bages=JewelleryBag.objects(category=request.json["category"])[precount:count]
    except:
        print("contnue..")
        if request.json["category"]=="":
            jewellery_bages=JewelleryBag.objects()
        else:
            jewellery_bages=JewelleryBag.objects(category=request.json["category"])
    if jewellery_bages:
        jewellery_bages=[jewellery_bag  for jewellery_bag in jewellery_bages if jewellery_bag.price in range(request.json["min"], request.json["max"]+1)] 
    
        return jsonify({"jewellery_bag": jewellery_bages}),200
    else: return jsonify({"jewellery_bages": []}),200

@app.route("/api/get-jewellery-bages-by-category", methods=["POST","GET"])
#@check_token
def get_all_jewellery_bages_by_category():
    '''
    Admin Api to Fetch all Normal jewellery_bages by category
    '''
    hack= request.data
    try:
        page = request.json.get('page')
        total_count= request.json["total_count"]
        precount = total_count * (page-1)
        count= total_count *page
        jewellery_bages=JewelleryBag.objects(category=request.json["category"])[precount:count]
    except:
        print("contnue..")
        jewellery_bages=JewelleryBag.objects(category=request.json["category"]) 
    if jewellery_bages:
        return jsonify({"jewellery_bages": jewellery_bages}),200
    else: return jsonify({"jewellery_bages": []}),200



@app.route("/api/admin/update-jewellery-bag", methods=["POST"])
@check_token
def update_jewellery_bag():
    '''
    Admin Api to update jewellery-bag

    '''
    user =User.objects(email=request.user['email']).first() 
    if user['role']=="admin":
        try: 
            jewellery_bag_items=request.json
            try:
                app_jewellery_bag=JewelleryBag.objects(id = request.json.get('_id')).first()
            except:
                return jsonify({"error":"jewellery_bag Not Found"}),404
            jewellery_bag = update_jewellery_box_helper(jewellery_bag_items, app_jewellery_bag)
            jewellery_bag.save()
            return jsonify({"message":"jewellery_bag Updated Successfully"}),200
        except Exception as e:
            return jsonify({"message": str(e)[:100]}),400      
    else:
        return jsonify({"message": "Unauthorized User"}),403


'''_____________________________________Test___________________________________________________ '''

#Api route to sign up a new user
@app.route('/api/signup', methods=["POST"])
def signup():
    email = request.json.get('email')
    password = request.json.get('password')
    if email is None or password is None:
        return {'message': 'Error missing email or password'},400
    try:
        user = pb.auth().create_user_with_email_and_password(email,password)
        return {'message': f'Successfully created user'},200
    except Exception as e:
        print(e)
        if "EMAIL_EXISTS" in str(e):
            return {'message': 'user Already Exist'},400
        traceback.print_exec()
        return {'message': 'Error creating user'},400
        

#Api route to get a new token for a valid user
@app.route('/api/token', methods=["POST"])
def token():
    email = request.json.get('email')
    password = request.json.get('password')
    try:
        user = pb.auth().sign_in_with_email_and_password(email, password)
        jwt = user['idToken']
        return {'token': jwt}, 200
    except:
        return {'message': 'There was an error logging in'},400
