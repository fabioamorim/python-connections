import pymongo 

# Get connection
def get_connection():

    server = 'localhost'
    port = '27017'

    client = pymongo.MongoClient(f"mongodb://{server}:{port}")

    return client 

# Select data
def select_data(db, collection):

    client = get_connection()

    db = client[db]
    collection = db[collection]

    for data in collection.find():
        print(data)

# Insert data
def insert_data(db, collection, data):
     
    client = get_connection()

    db = client[db]
    collection = db[collection]

    collection.insert_one(data)

# Delete data
def delete_data(db, collection, query):

    client = get_connection()

    db = client[db]
    collection = db[collection]

    collection.delete_one(query)
    
def update_data(db, collection, query, newvalues):

    client = get_connection()

    db = client[db]
    collection = db[collection]

    collection.update_one(query, newvalues)

