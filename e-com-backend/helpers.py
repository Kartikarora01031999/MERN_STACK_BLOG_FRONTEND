from models import *
from bson.objectid import ObjectId
import datetime

''' jewellery_box HELPERS '''

def add_jewellery_box_helper(jewellery_box_items, model):
    '''
    Function to Add jewellery_box 
    
    '''
    name = jewellery_box_items.get('name') #required 
    description = jewellery_box_items.get("description") or ""
    price = jewellery_box_items.get("price") or 0.0#required 
    limit = jewellery_box_items.get('type') or 10
    category = jewellery_box_items.get("category") or ""
    size = jewellery_box_items.get('size') or ""
    quantity = jewellery_box_items.get('quantity') or 0 #required 
    sold= jewellery_box_items.get('sold') or 0
    image = jewellery_box_items.get('image') #required 
    inStock = jewellery_box_items.get('inStock') or True
    
    if model =="JewelleryBox":

        return JewelleryBox(name = name,
        price = price,
        category = category,
        description = description,
        size = size,
        quantity = quantity,
        sold = sold,
        image = image,
        limit = limit,
        inStock=inStock)
    
    if model =="JewelleryBag":

        return JewelleryBag(name = name,
        price = price,
        category = category,
        description = description,
        size = size,
        quantity = quantity,
        sold = sold,
        image = image,
        limit = limit,
        inStock=inStock)
    
def update_jewellery_box_helper(jewellery_box_items, jewellery_box):
    '''
    Function to Update jewellery_box 
    
    '''

    if 'name' in jewellery_box_items.keys(): jewellery_box.name = jewellery_box_items["name"]
    if 'price' in jewellery_box_items.keys(): jewellery_box.price = jewellery_box_items["price"]
    if 'category' in jewellery_box_items.keys(): jewellery_box.category = jewellery_box_items["category"]
    if 'description' in jewellery_box_items.keys(): jewellery_box.description = jewellery_box_items["description"]
    if 'size' in jewellery_box_items.keys(): jewellery_box.size = jewellery_box_items["size"]
    if 'quantity' in jewellery_box_items.keys(): jewellery_box.quantity = jewellery_box_items["quantity"]
    if 'sold' in jewellery_box_items.keys(): jewellery_box.sold = jewellery_box_items["sold"]
    if 'image' in jewellery_box_items.keys(): jewellery_box.image = jewellery_box_items["image"]
    if 'limit' in jewellery_box_items.keys(): jewellery_box.limit = jewellery_box_items["limit"]
    if 'inStock' in jewellery_box_items.keys(): jewellery_box.inStock = jewellery_box_items["inStock"]
    jewellery_box.modified_at = datetime.datetime.now().isoformat()
    return jewellery_box

    





''' ORDER HELPERS '''

def add_order_helper(order_item, email):
    '''
    Function to Add Order
    '''

    payment_intent={}
    order_jewellery_box=order_item["jewellery_boxs"]
    if email == None :
        order_by ="Guest User"
        if "email" in order_item.keys(): order_by=order_item["email"]
    else:
        user=  User.objects(email=email).first()
        order_by= str(user.id)

    if "payment" in order_item: payment_intent=order_item["payment"]
    if "type" in order_item.keys(): order_type=order_item["type"] 
    else: order_type="normal"
    if "fabric" in order_item.keys(): order_fabric =order_item["fabric"]
    else: order_fabric=""
    if "color" in order_item.keys(): order_color =order_item["color"]
    else: order_color=""
    if "price" in order_item.keys(): order_price =order_item["price"]
    else: order_price= 0.0
    if "address" in order_item.keys(): order_address =order_item["address"]
    else: order_address="Not Updated"
    if "phone" in order_item.keys(): order_phone= order_item["phone"]
    else : order_phone= "Not updated"
    if "size" in order_item.keys(): order_size =order_item["size"]
    else: order_size= " "
    if "quantity" in order_item.keys(): order_quantity = order_item["quantity"]
    else: order_quantity= 1
    
    return Order(order_jewellery_box=order_jewellery_box,
        payment_intent=payment_intent,
        order_by=order_by,
        order_type=order_type,
        order_fabric=order_fabric,
        order_color=order_color,
        order_price=order_price,
        order_address=order_address,
        order_phone= order_phone,
        order_size= order_size,
        order_quantity= order_quantity)




''' CART HELPERS '''


def add_cart_helper(cart_items):
    '''
    Function to Add to Cart
    '''
    cart_jewellery_box = cart_items["jewellery_boxs"]
    cart_total = cart_items["total_price"]

    return Cart(cart_jewellery_box = cart_jewellery_box,
        cart_total = cart_total)

def update_cart_helper(cart_items):
    '''
    Function to Update Cart
    '''
    cart=Cart.objects(id = cart_items["id"]).first()
    cart.cart_total=cart_items["total_price"]
    cart.cart_jewellery_box.clear()
    for i in cart_items["jewellery_boxs"]:
        try:
            i["_id"]=ObjectId(i["_id"]["$oid"])
            print(i["_id"])
        except:
            continue
    cart.cart_jewellery_box= cart_items["jewellery_boxs"]
    return cart

