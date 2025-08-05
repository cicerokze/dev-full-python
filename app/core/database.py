from motor.motor_asyncio import AsyncIOMotorClient
import os

client = AsyncIOMotorClient(os.getenv("MONGODB_URL"))
db = client.get_database("EcommerceDB")

orders_collection = db.get_collection("Orders")
items_collection = db.get_collection("Items")
users_collection = db.get_collection("Users")
products_collection = db.get_collection("Products")
categories_collection = db.get_collection("Categories")