import json
from urllib.request import DataHandler
from flask import Flask, request, jsonify, redirect, session, make_response, render_template, url_for
from flask_session import Session
from flask_mongoengine import MongoEngine
import cloudinary
import cloudinary.uploader
import pymongo
from pymongo import MongoClient
import urllib
from bson.json_util import dumps,loads
''' firebase modules '''
import os
import firebase_admin
from firebase_admin import credentials,auth
from firebase import Firebase
import traceback
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

creare_db = cluster["EcomDataBase"]
load_dotenv()
firebaseConfig =json.load(open('./fbconfig.json'))


print(firebaseConfig)
pb = Firebase(firebaseConfig)

sendgrid_api_key = os.getenv('SENDGRID_API_KEY')