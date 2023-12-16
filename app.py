from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from Crypto.Cipher import AES
from flask_migrate import Migrate
from Crypto.Util.Padding import pad, unpad
import base64
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/db_employee'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db) 

SECRET_KEY = b'secretkey1234567' 
# SECRET_KEY = b'YourSecretKey1234YourSecretKey1234'

cipher = AES.new(SECRET_KEY, AES.MODE_CBC, iv=b'1234567890123456' )

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(35), nullable=False)
    gender = db.Column(db.String(15), nullable=False)
    status = db.Column(db.String(15), nullable=False)



encrypt_cipher = AES.new(SECRET_KEY, AES.MODE_CBC, iv=b'1234567890123456' )
decrypt_cipher = AES.new(SECRET_KEY, AES.MODE_CBC, iv=b'1234567890123456' )


def encrypt(text):
    ct_bytes = encrypt_cipher.encrypt(pad(text.encode('utf-8'), 16))
    return base64.b64encode(ct_bytes).decode('utf-8')

def decrypt(text):
    ct = base64.b64decode(text)
    pt = unpad(decrypt_cipher.decrypt(ct), 16)
    return pt.decode('utf-8')


@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = Employee(username=data['username'], password=encrypt(data['password']),first_name=data['first_name'],last_name=data['last_name'],gender=data['gender'],status=data['status'] )
    a = encrypt(data['password'])
    print(a)
    b = decrypt(a)
    print(b)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'status': 'Success','message': 'Success created',}), 201

@app.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    user = Employee.query.get(user_id)
    print(user.password)
    a = user.password
    decrypted_password = decrypt(a)
    return jsonify({'id': user.id, 'username': user.username, 'password': decrypted_password, 'first_name': user.first_name, 'last_name': user.last_name, 'gender': user.gender, 'status': user.status})

@app.route('/users', methods=['GET'])
def get_all_users():
    users = Employee.query.all()
    user_list = []

    for user in users:
        decrypted_password = decrypt(user.password)
        user_data = {'id': user.id, 'username': user.username, 'password': decrypted_password, 'first_name': user.first_name, 'last_name': user.last_name, 'gender': user.gender, 'status': user.status}
        user_list.append(user_data)

    return jsonify({'users': user_list})


@app.route('/user/<user_id>', methods=['PUT'])
def update_user(user_id):
    user = Employee.query.get(user_id)
    data = request.get_json()
    user.username = data['username']
    user.password = encrypt(data['password'])
    user.first_name = data['first_name']
    user.last_name = data['last_name']
    user.gender = data['gender']
    user.status = data['status']
    db.session.commit()
    return jsonify({'message': 'User updated successfully','status':'Success'})

@app.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = Employee.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully','status':'Success'})

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
