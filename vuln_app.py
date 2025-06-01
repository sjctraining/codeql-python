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

# 🚨 Vulnerability 4: Insecure deserialization
@app.route('/deserialize', methods=['POST'])
def deserialize():
    import pickle
    data = request.data
    obj = pickle.loads(data)
    return str(obj)

# 🚨 Vulnerability 5: Insecure use of eval
@app.route('/eval', methods=['GET'])
def evaluate():
    expr = request.args.get('expr', '')
    return str(eval(expr))

# 🚨 Vulnerability 6: Poor authentication check
@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('username')
    pwd = request.form.get('password')
    if user == USERNAME and pwd == PASSWORD:
        return "Login successful!"
    else:
        return "Invalid credentials"

# 🚨 Vulnerability 7: Sensitive data exposure
@app.route('/debug', methods=['GET'])
def debug():
    return f"Debug info: USERNAME={USERNAME}, PASSWORD={PASSWORD}"

# 🚨 Vulnerability 8: Unvalidated redirect
@app.route('/redirect', methods=['GET'])
def redirect_user():
    from flask import redirect
    target = request.args.get('url')
    return redirect(target)

if __name__ == '__main__':
    app.run(debug=True)
