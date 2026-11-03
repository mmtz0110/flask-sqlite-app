import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row  # Mengembalikan hasil query sebagai dictionary-like object
    return conn

@app.route('/')
def index():
    return jsonify({"status": "online", "message": "Flask + SQLite API is running"})

@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return jsonify([dict(u) for u in users])

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or 'username' not in data or 'email' not in data:
        return jsonify({"error": "Data username dan email wajib diisi"}), 400

    conn = get_db_connection()
    try:
        conn.execute('INSERT INTO users (username, email) VALUES (?, ?)',
                     (data['username'], data['email']))
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        return jsonify({"error": "Username sudah terdaftar"}), 409

    conn.close()
    return jsonify({"message": "User berhasil ditambahkan"}), 201

if __name__ == '__main__':
    app.run(debug=True)