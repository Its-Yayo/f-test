#!/usr/bin/python3

from flask import Flask, render_template, request, redirect, url_for, flash, session
from dotenv import load_dotenv
import mariadb
import sys
import os

app = Flask(__name__)
load_dotenv()

def connection() -> None:
    config = {
        'host': os.getenv('DB_HOST'),
        'port': int(os.getenv('DB_PORT')),
        'user': os.getenv('DB_USERNAME'),
        'password': os.getenv('DB_PASSWORD'),
        'database': os.getenv('DB_NAME')
    }

    try:
        conn = mariadb.connect(**config)
        cursor = conn.cursor()
        print("Connected to MariaDB F-Test") # Debug Message
        return conn
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

@app.route("/add_user", methods=['POST'])
def add_user() -> str:
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']

        return "Done"
@app.route("/")
def main() -> str:
    return render_template('index.html')

if __name__ == '__main__':
    connection()
    app.run()
    sys.exit(1)

