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
      "first_name": "Alice",
      "last_name": "Smith",
      "email": "alice@example.com",
    },
    {
      "first_name": "Bob",
      "last_name": "Johnson",
      "email": "bob@example.com",
    },
    {
      "first_name": "Charlie",
      "last_name": "Brown",
      "email": "charlie@example.com",
    },
    {
      "first_name": "David",
      "last_name": "Williams",
      "email": "david@example.com",
    },
    {
      "first_name": "Eve",
      "last_name": "Davis",
      "email": "eve@example.com",
    }
]);

db.getCollection('Categories').insertMany([
    {"name": "Vestuario", "description": "Vestuario e acessórios para o dia a dia."},
    {"name": "Calçados", "description": "Calçados para todas as ocasiões."},
    {"name": "Eletrônicos", "description": "Dispositivos eletrônicos e gadgets."},
    {"name": "Informática", "description": "Produtos de informática e tecnologia."},
    {"name": "Móveis", "description": "Móveis e decoração para sua casa."},
    {"name": "Livros e Papelaria", "description": "Livros, cadernos e material escolar."},
    {"name": "Acessórios", "description": "Acessórios diversos para o dia a dia."},
    {"name": "Eletrodomésticos", "description": "Eletrodomésticos para sua cozinha."},
    {"name": "Casa e Jardim", "description": "Produtos para casa e jardim."},
]);

db.getCollection('Orders').insertMany([
    {
      "customer_name": "Alice",
      "customer_email": "alice@example.com",
      "items": [
        {"item_id": 1, "name": "Basic T-shirt", "category": "Clothing", "quantity": 1, "unit_price": 45.90},
        {"item_id": 2, "name": "Jeans", "category": "Clothing", "quantity": 1, "unit_price": 129.90},
        {"item_id": 3, "name": "Sports Shoes", "category": "Footwear", "quantity": 2, "unit_price": 249.00}
      ],
      "price": 45.90,
      "date": new Date().toISOString(),
    },
    {
      "customer_name": "Bob",
      "customer_email": "bob@example.com",
      "items": [
        {"item_id": 1, "name": "Basic T-shirt", "category": "Clothing", "quantity": 2, "unit_price": 45.90},
        {"item_id": 2, "name": "Jeans", "category": "Clothing", "quantity": 1, "unit_price": 129.90},
        {"item_id": 3, "name": "Sports Shoes", "category": "Footwear", "quantity": 2, "unit_price": 249.00}
      ],
      "price": 129.90,
      "date": new Date().toISOString(),
    },
    {
      "customer_name": "Charlie",
      "customer_email": "charlie@example.com",
      "items": [
        {"item_id": 3, "name": "Sports Shoes", "category": "Footwear", "quantity": 1, "unit_price": 249.00}
      ],
      "price": 249.00,
      "date": new Date().toISOString(),
    },
    {
      "customer_name": "David",
      "customer_email": "david@example.com",
      "items": [
        {"item_id": 4, "name": "Bluetooth Headphones", "category": "Electronics", "quantity": 2, "unit_price": 180.50}
      ],
      "price": 180.50,
      "date": new Date().toISOString(),
    },
    {
      "customer_name": "Eve",
      "customer_email": "eve@example.com",
      "items": [
        {"item_id": 5, "name": "Wireless Mouse", "category": "Computers", "quantity": 3, "unit_price": 75.00}
      ],
      "price": 75.00,
      "date": new Date().toISOString(),
    }
]);

db.getCollection('Products').insertMany([
    {"name": "Basic T-shirt", "category": "Clothing", "unit_price": 45.90},
    {"name": "Jeans", "category": "Clothing", "unit_price": 129.90},
    {"name": "Sports Shoes", "category": "Footwear", "unit_price": 249.00},
    {"name": "Bluetooth Headphones", "category": "Electronics", "unit_price": 180.50},
    {"name": "Wireless Mouse", "category": "Computers", "unit_price": 75.00},
    {"name": "Mechanical Keyboard", "category": "Computers", "unit_price": 320.00},
    {"name": "24-inch monitor", "category": "Electronics", "unit_price": 899.00},
    {"name": "HD webcam", "category": "Computers", "unit_price": 99.00},
    {"name": "Desktop microphone", "category": "Electronics", "unit_price": 150.00},
    {"name": "Ergonomic office chair", "category": "Furniture", "unit_price": 550.00},
    {"name": "Book (Fiction)", "category": "Books and Stationery", "unit_price": 59.90},
    {"name": "University Notebook", "category": "Books and Stationery", "unit_price": 22.50},
    {"name": "Ballpoint Pen", "category": "Books and Stationery", "unit_price": 3.80},
    {"name": "School Backpack", "category": "Accessories", "unit_price": 85.00},
    {"name": "Thermos", "category": "Household Goods", "unit_price": 65.00},
    {"name": "Electric Coffee Maker", "category": "Appliances", "unit_price": 199.90},
    {"name": "Toaster", "category": "Appliances", "unit_price": 110.00},
    {"name": "Blender", "category": "Appliances", "unit_price": 160.00},
    {"name": "Table Fan", "category": "Appliances", "unit_price": 95.00},
    {"name": "Smartwatch", "category": "Electronics", "unit_price": 650.00},
]);

db.getCollection('Items').insertMany([
    {"name": "Basic T-shirt", "category": "Clothing", "unit_price": 45.90},
    {"name": "Jeans", "category": "Clothing", "unit_price": 129.90},
    {"name": "Sports Shoes", "category": "Footwear", "unit_price": 249.00},
    {"name": "Bluetooth Headphones", "category": "Electronics", "unit_price": 180.50},
    {"name": "Wireless Mouse", "category": "Computers", "unit_price": 75.00},
    {"name": "Mechanical Keyboard", "category": "Computers", "unit_price": 320.00},
    {"name": "24-inch monitor", "category": "Electronics", "unit_price": 899.00},
    {"name": "HD webcam", "category": "Computers", "unit_price": 99.00},
    {"name": "Desktop microphone", "category": "Electronics", "unit_price": 150.00},
    {"name": "Ergonomic office chair", "category": "Furniture", "unit_price": 550.00},
    {"name": "Book (Fiction)", "category": "Books and Stationery", "unit_price": 59.90},
    {"name": "University Notebook", "category": "Books and Stationery", "unit_price": 22.50},
    {"name": "Ballpoint Pen", "category": "Books and Stationery", "unit_price": 3.80},
    {"name": "School Backpack", "category": "Accessories", "unit_price": 85.00},
    {"name": "Thermos", "category": "Household Goods", "unit_price": 65.00},
    {"name": "Electric Coffee Maker", "category": "Appliances", "unit_price": 199.90},
    {"name": "Toaster", "category": "Appliances", "unit_price": 110.00},
    {"name": "Blender", "category": "Appliances", "unit_price": 160.00},
    {"name": "Table Fan", "category": "Appliances", "unit_price": 95.00},
    {"name": "Smartwatch", "category": "Electronics", "unit_price": 650.00},
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
