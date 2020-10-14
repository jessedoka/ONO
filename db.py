import ssl
from pymongo import MongoClient
from werkzeug.security import generate_password_hash

from user import User

client = MongoClient(
    "mongodb+srv://Jesse:SbjZHADI2ze5Ed6y@ono.s8dnu.mongodb.net/ChatDB?retryWrites=true&w=majority", 
    ssl = True,
    ssl_cert_reqs=ssl.CERT_NONE
    )

chat_db = client.get_database('ChatDB')
users_collection = chat_db.get_collection("users")

def save_user(username, email, password): 
    password_hash = generate_password_hash(password)
    users_collection.insert_one({
        '_id': username,
        'email': email,
        'password': password_hash
    })

def get_user(username):
    user_data = users_collection.find_one({
        '_id': username
    })
    if user_data:
        return User(user_data['_id'], user_data['email'], user_data['password'])
    else:
        None
    
if __name__ == "__main__": 
    save_user("derik", "derick123@gmail.com", "froggit42")
    
 