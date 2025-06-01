import os
import subprocess
import sqlite3
from flask import Flask, request

app = Flask(__name__)

# 🚨 Vulnerability 1: Hardcoded credentials
USERNAME = "admin"
PASSWORD = "password123"

# 🚨 Vulnerability 2: SQL Injection
def get_user_info(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchall()

# 🚨 Vulnerability 3: Command Injection
@app.route('/ping', methods=['GET'])
def ping():
    host = request.args.get('host', '')
    response = os.popen(f"ping -c 1 {host}").read()
    return response
