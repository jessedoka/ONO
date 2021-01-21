from werkzeug.security import generate_password_hash
from datetime import datetime, timedelta
from Vault.vault import Metavault as MV
from user import User

net = MV('ONOchatDB', 'user_accounts.json')
connection = net.connnection()
if connection:
    print('Created')

def save_user(username:  str, email: str, password: str):
    password_hash = generate_password_hash(password)
    net.insert_object({
        '_id': username,
        'email': email,
        'password': password_hash
    })
