# from flask import Flask, request
# from flask_restful import Api, Resource
# import psycopg2

# app = Flask(__name__)
# api = Api(app)

# # Konfigurasi PostgreSQL
# conn = psycopg2.connect(
#     database="db_loginuser",
#     user="postgres",
#     password="postgres",
#     host="localhost",  
#     port="5432"
# )
# cursor = conn.cursor()

# class UserResource(Resource):
#     def post(self):
#         data = request.get_json()

#         username = data.get('username')
#         password = data.get('password')
#         name = data.get('name')
#         email = data.get('email')

#         # Simpan user ke database
#         cursor.execute("INSERT INTO users2 (username, password, name, email) VALUES (%s, %s, %s, %s)",
#                        (username, password, name, email))
#         conn.commit()

#         return {'message': 'User berhasil didaftarkan'}, 201

# api.add_resource(UserResource, '/users2')

# if __name__ == '__main__':
#     app.run(debug=True)
