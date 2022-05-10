import mongoengine as me
import datetime
from enum import Enum

class User(me.Document):
    name = me.StringField()
    email=me.StringField(required = True, unique= True)
    role = me.StringField(default = "user")
    cart = me.StringField(default= "")
    address = me.StringField()
    phone_number= me.StringField()
    business_name= me.StringField()
    gst_in=me.StringField()
    # wishlist= me.ReferenceField(Product)
    created_at = me.StringField(required=True, default= datetime.datetime.now().isoformat())
    modified_at = me.StringField(required=True, default= datetime.datetime.now().isoformat())


class Cart(me.Document):
    cart_product = me.ListField(required=True)
    cart_total = me.IntField(required=True)
    created_at = me.StringField(default= datetime.datetime.now().isoformat())
    modified_at = me.StringField(default= datetime.datetime.now().isoformat())

class Status(Enum):
    NOT_PROCESSED = "Not Processed"
    PROCESSING = "Processing"
    DISPATCHED = "Dispatched"
    CANCELLED  = "Cancelled"
    COMPLETED  = "Completed"

class Order(me.Document):
    order_product = me.ListField(required=True)
    payment_intent = me.DictField(required= True)
    order_status = me.EnumField(Status, default=Status.NOT_PROCESSED)
    order_by = me.StringField()
    order_type= me.StringField(required=True ,default= "normal") #virtual_product
    order_price = me.FloatField(required= True)#virtual_product
    order_address = me.StringField(required=True)
    order_phone = me.StringField(required= True)
    order_quantity= me.IntField(required=True, default=1)
    order_size =me.StringField(required= True)
    created_at = me.StringField(default= datetime.datetime.now().isoformat())
    modified_at = me.StringField(default= datetime.datetime.now().isoformat())

class JewelleryBox(me.Document):
    name=me.StringField(required=True, unique=True)
    description= me.StringField()
    price = me.FloatField(required=True)
    limit=me.IntField()
    category=me.StringField()
    size=me.StringField()
    sold= me.IntField(default=0)
    inStock = me.BooleanField(default=True)
    image=me.ListField(required=True)
    quantity=me.IntField(required=True)
    created_at = me.StringField(default= datetime.datetime.now().isoformat())
    modified_at = me.StringField(default= datetime.datetime.now().isoformat())

class JewelleryBag(me.Document):
    name=me.StringField(required=True, unique=True)
    description= me.StringField()
    price = me.FloatField(required=True)
    limit=me.IntField()
    category=me.StringField()
    size=me.StringField()
    sold= me.IntField(default=0)
    inStock = me.BooleanField(default=True)
    image=me.ListField(required=True)
    quantity=me.IntField(required=True)
    created_at = me.StringField(default= datetime.datetime.now().isoformat())
    modified_at = me.StringField(default= datetime.datetime.now().isoformat())




