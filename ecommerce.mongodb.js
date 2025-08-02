/* global use, db */
// MongoDB Playground
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.

// Create a new database.
const database = 'EcommerceDB';
use(database);

// Create a new collections.
const users = 'Users';
const categories = 'Categories';
const items = 'Items';
const products = 'Products';
const orders = 'Orders';

db.createCollection(users);
db.createCollection(categories);
db.createCollection(products);
db.createCollection(items);
db.createCollection(orders);

// Insert sample data into the collections.
db.getCollection('Users').insertMany([
    {
      "user_id": 1,
      "first_name": "Alice",
      "last_name": "Smith",
      "email": "alice@example.com",
    },
    {
      "user_id": 2,
      "first_name": "Bob",
      "last_name": "Johnson",
      "email": "bob@example.com",
    },
    {
      "user_id": 3,
      "first_name": "Charlie",
      "last_name": "Brown",
      "email": "charlie@example.com",
    },
    {
      "user_id": 4,
      "first_name": "David",
      "last_name": "Williams",
      "email": "david@example.com",
    },
    {
      "user_id": 5,
      "first_name": "Eve",
      "last_name": "Davis",
      "email": "eve@example.com",
    }
]);

db.getCollection('Categories').insertMany([
    {"category_id": 1, "name": "Vestuario", "description": "Vestuario e acessórios para o dia a dia."},
    {"category_id": 2, "name": "Calçados", "description": "Calçados para todas as ocasiões."},
    {"category_id": 3, "name": "Eletrônicos", "description": "Dispositivos eletrônicos e gadgets."},
    {"category_id": 4, "name": "Informática", "description": "Produtos de informática e tecnologia."},
    {"category_id": 5, "name": "Móveis", "description": "Móveis e decoração para sua casa."},
    {"category_id": 6, "name": "Livros e Papelaria", "description": "Livros, cadernos e material escolar."},
    {"category_id": 7, "name": "Acessórios", "description": "Acessórios diversos para o dia a dia."},
    {"category_id": 8, "name": "Eletrodomésticos", "description": "Eletrodomésticos para sua cozinha."},
    {"category_id": 9, "name": "Casa e Jardim", "description": "Produtos para casa e jardim."},
]);

db.getCollection('Orders').insertMany([
    {
      "order_id": 1,
      "customer_name": "Alice",
      "customer_email": "alice@example.com",
      "items": [
        {"item_id": 1, "name": "Basic T-shirt", "category": "Clothing", "unit_price": 45.90},
        {"item_id": 2, "name": "Jeans", "category": "Clothing", "unit_price": 129.90},
        {"item_id": 3, "name": "Sports Shoes", "category": "Footwear", "unit_price": 249.00}
      ],
      "price": 45.90,
      "date": new Date('2024-01-15')
    },
    {
      "order_id": 2,
      "customer_name": "Bob",
      "customer_email": "bob@example.com",
      "items": [
        {"item_id": 1, "name": "Basic T-shirt", "category": "Clothing", "unit_price": 45.90},
        {"item_id": 2, "name": "Jeans", "category": "Clothing", "unit_price": 129.90},
        {"item_id": 3, "name": "Sports Shoes", "category": "Footwear", "unit_price": 249.00}
      ],
      "price": 129.90,
      "date": new Date('2024-01-16')
    },
    {
      "order_id": 3,
      "customer_name": "Charlie",
      "customer_email": "charlie@example.com",
      "items": [
        {"item_id": 3, "name": "Sports Shoes", "category": "Footwear", "unit_price": 249.00}
      ],
      "price": 249.00,
      "date": new Date('2024-01-17')
    },
    {
      "order_id": 4,
      "customer_name": "David",
      "customer_email": "david@example.com",
      "items": [
        {"item_id": 4, "name": "Bluetooth Headphones", "category": "Electronics", "unit_price": 180.50}
      ],
      "price": 180.50,
      "date": new Date('2024-01-18')
    },
    {
      "order_id": 5,
      "customer_name": "Eve",
      "customer_email": "eve@example.com",
      "items": [
        {"item_id": 5, "name": "Wireless Mouse", "category": "Computers", "unit_price": 75.00}
      ],
      "price": 75.00,
      "date": new Date('2024-01-19')
    }
]);

db.getCollection('Products').insertMany([
    {"product_id": 1, "name": "Basic T-shirt", "category": "Clothing", "unit_price": 45.90},
    {"product_id": 2, "name": "Jeans", "category": "Clothing", "unit_price": 129.90},
    {"product_id": 3, "name": "Sports Shoes", "category": "Footwear", "unit_price": 249.00},
    {"product_id": 4, "name": "Bluetooth Headphones", "category": "Electronics", "unit_price": 180.50},
    {"product_id": 5, "name": "Wireless Mouse", "category": "Computers", "unit_price": 75.00},
    {"product_id": 6, "name": "Mechanical Keyboard", "category": "Computers", "unit_price": 320.00},
    {"product_id": 7, "name": "24-inch monitor", "category": "Electronics", "unit_price": 899.00},
    {"product_id": 8, "name": "HD webcam", "category": "Computers", "unit_price": 99.00},
    {"product_id": 9, "name": "Desktop microphone", "category": "Electronics", "unit_price": 150.00},
    {"product_id": 10, "name": "Ergonomic office chair", "category": "Furniture", "unit_price": 550.00},
    {"product_id": 11, "name": "Book (Fiction)", "category": "Books and Stationery", "unit_price": 59.90},
    {"product_id": 12, "name": "University Notebook", "category": "Books and Stationery", "unit_price": 22.50},
    {"product_id": 13, "name": "Ballpoint Pen", "category": "Books and Stationery", "unit_price": 3.80},
    {"product_id": 14, "name": "School Backpack", "category": "Accessories", "unit_price": 85.00},
    {"product_id": 15, "name": "Thermos", "category": "Household Goods", "unit_price": 65.00},
    {"product_id": 16, "name": "Electric Coffee Maker", "category": "Appliances", "unit_price": 199.90},
    {"product_id": 17, "name": "Toaster", "category": "Appliances", "unit_price": 110.00},
    {"product_id": 18, "name": "Blender", "category": "Appliances", "unit_price": 160.00},
    {"product_id": 19, "name": "Table Fan", "category": "Appliances", "unit_price": 95.00},
    {"product_id": 20, "name": "Smartwatch", "category": "Electronics", "unit_price": 650.00},
]);

db.getCollection('Items').insertMany([
    {"item_id": 1, "name": "Basic T-shirt", "category": "Clothing", "unit_price": 45.90},
    {"item_id": 2, "name": "Jeans", "category": "Clothing", "unit_price": 129.90},
    {"item_id": 3, "name": "Sports Shoes", "category": "Footwear", "unit_price": 249.00},
    {"item_id": 4, "name": "Bluetooth Headphones", "category": "Electronics", "unit_price": 180.50},
    {"item_id": 5, "name": "Wireless Mouse", "category": "Computers", "unit_price": 75.00},
    {"item_id": 6, "name": "Mechanical Keyboard", "category": "Computers", "unit_price": 320.00},
    {"item_id": 7, "name": "24-inch monitor", "category": "Electronics", "unit_price": 899.00},
    {"item_id": 8, "name": "HD webcam", "category": "Computers", "unit_price": 99.00},
    {"item_id": 9, "name": "Desktop microphone", "category": "Electronics", "unit_price": 150.00},
    {"item_id": 10, "name": "Ergonomic office chair", "category": "Furniture", "unit_price": 550.00},
    {"item_id": 11, "name": "Book (Fiction)", "category": "Books and Stationery", "unit_price": 59.90},
    {"item_id": 12, "name": "University Notebook", "category": "Books and Stationery", "unit_price": 22.50},
    {"item_id": 13, "name": "Ballpoint Pen", "category": "Books and Stationery", "unit_price": 3.80},
    {"item_id": 14, "name": "School Backpack", "category": "Accessories", "unit_price": 85.00},
    {"item_id": 15, "name": "Thermos", "category": "Household Goods", "unit_price": 65.00},
    {"item_id": 16, "name": "Electric Coffee Maker", "category": "Appliances", "unit_price": 199.90},
    {"item_id": 17, "name": "Toaster", "category": "Appliances", "unit_price": 110.00},
    {"item_id": 18, "name": "Blender", "category": "Appliances", "unit_price": 160.00},
    {"item_id": 19, "name": "Table Fan", "category": "Appliances", "unit_price": 95.00},
    {"item_id": 20, "name": "Smartwatch", "category": "Electronics", "unit_price": 650.00},
]);

// The prototype form to create a collection:
/* db.createCollection( <name>,
  {
    capped: <boolean>,
    autoIndexId: <boolean>,
    size: <number>,
    max: <number>,
    storageEngine: <document>,
    validator: <document>,
    validationLevel: <string>,
    validationAction: <string>,
    indexOptionDefaults: <document>,
    viewOn: <string>,
    pipeline: <pipeline>,
    collation: <document>,
    writeConcern: <document>,
    timeseries: { // Added in MongoDB 5.0
      timeField: <string>, // required for time series collections
      metaField: <string>,
      granularity: <string>,
      bucketMaxSpanSeconds: <number>, // Added in MongoDB 6.3
      bucketRoundingSeconds: <number>, // Added in MongoDB 6.3
    },
    expireAfterSeconds: <number>,
    clusteredIndex: <document>, // Added in MongoDB 5.3
  }
)*/

// More information on the `createCollection` command can be found at:
// https://www.mongodb.com/docs/manual/reference/method/db.createCollection/
