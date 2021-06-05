import ssl
from config import client
from werkzeug.security import generate_password_hash
from datetime import datetime, timedelta

from user import User

chat_db = client.get_database('CHAT_DB')
users_collection = chat_db.get_collection("users")
message_collection = chat_db.get_collection("messages")


def save_user(username: str, email: str, password: str): 
    password_hash = generate_password_hash(password)
    users_collection.insert_one({
        '_id': username,
        'email': email,
        'password': password_hash
    })

def save_message(username, room, message, time=datetime.now()):
    message_collection.insert_one({
        'id': username,
        'message': message,
        'room': room,
        'time': time
    })

def get_user(username):
    user_data = users_collection.find_one({
        '_id': username
    })
    if user_data:
        return User(user_data['_id'], user_data['email'], user_data['password'])
    else:
        None

def timeformat(time):
    now = datetime.now()
    time_delta = (now - time)
    sec_diff = time_delta.total_seconds()
    return sec_diff/60**2

    
if __name__ == "__main__": 
    save_user('test', 'test@icloud.com', 'test')
