import json
import re
from urllib.request import DataHandler
from flask import Flask, request, jsonify, redirect, session, make_response, render_template, url_for
from flask_session import Session
from flask_mongoengine import MongoEngine
import cloudinary
import cloudinary.uploader
import pymongo
from pymongo import MongoClient, ReturnDocument
import urllib
from bson.json_util import dumps,loads
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

User = ecom_db["User"]
JewelleryBox = ecom_db["JewelleryBox"]
JewelleryBag = ecom_db["JewelleryBag"]

#Wrap check token
def check_token(f):
    '''
    Middle Ware to check Auth Token

    '''

    def wrap(*args,**kwargs):
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
    name = request.json["name"]
    user=User.find_one_and_update({"email": email},{"$set":{"name":name, "email":email}}, return_document=ReturnDocument.AFTER)
    if user:
        return jsonify({"data": user}),200
    else:
        doc={'_id': uuid.uuid4().hex,
        'name': name,
        'email':email,
        'phone_number':"",
        'user_type':'user',
        "business_name":"",
        "GSTIn":"",
        "cart_id":"",
        "Address":""
        }
        user=User.insert_one(doc)
        return jsonify({"message": "User Created"}),200




#current user
@app.route("/api/current-user", methods=["POST"])
@check_token
def current_user():
    '''
    Api to fetch Current User 

    '''
    current_user =json.loads(dumps(User.find_one({'email': request.user["email"]}))) 
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
