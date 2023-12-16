# from flask import Flask, request, jsonify
# import psycopg2
# from psycopg2 import sql

# app = Flask(__name__)

# # Konfigurasi PostgreSQL
# db_config = {
#     'host': 'localhost',
#     'dbname': 'db_loginuser',
#     'user': 'postgres',
#     'password': 'postgres',
# }

# # Fungsi bantu untuk membuat koneksi ke PostgreSQL
# def create_connection():
#     return psycopg2.connect(**db_config)

# # Endpoint untuk login
# @app.route('/login', methods=['POST'])
# def login():
#     try:
#         # Ambil data dari request
#         data = request.get_json()
#         username = data['username']
#         password = data['password']

#         # Buat koneksi ke database
#         conn = create_connection()
#         cursor = conn.cursor()

#         # Cek apakah username dan password valid
#         query = sql.SQL("SELECT * FROM users2 WHERE username={} AND password={}").format(
#             sql.Literal(username),
#             sql.Literal(password),
#         )
#         cursor.execute(query)
#         user = cursor.fetchone()

#         if user is not None:
#             # Data tersedia
#             result = {'status': 'success', 'message': 'Login berhasil'}
#         else:
#             # Data tidak tersedia
#             result = {'status': 'fail', 'message': 'Login gagal'}

#         # Tutup koneksi
#         cursor.close()
#         conn.close()

#         return jsonify(result)

#     except Exception as e:
#         return jsonify({'status': 'error', 'message': str(e)})

# if __name__ == '__main__':
#     app.run(debug=True)
