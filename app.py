#!/usr/bin/python3

from flask import Flask, Response, render_template, request, redirect, url_for, session
from dotenv import load_dotenv
import mariadb
import sys
import os

app = Flask(__name__)
load_dotenv()


def connection() -> mariadb.Connection:
    config = {
        'host': os.getenv('DB_HOST'),
        'port': int(os.getenv('DB_PORT')),
        'user': os.getenv('DB_USERNAME'),
        'password': os.getenv('DB_PASSWORD'),
        'database': os.getenv('DB_NAME')
    }

    try:
        conn = mariadb.connect(**config)
        print("Connected")  # Debug Message
        return conn
    except mariadb.Error as e:
        print(f"Error Connecting: {e}")
        sys.exit(1)


@app.route("/add_user", methods=['POST'])
def add_user() -> str:
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']

        conn = None

        try:
            conn = connection()
            cur = conn.cursor()
            cur.callproc('insertContact', (fullname, phone, email))
            conn.commit()
            conn.close()
            return "Success"
        except mariadb.Error as e:
            print(f"Error executing SQL: {e}")
            return "Error"
        finally:
            if conn:
                conn.close()


@app.route("/")
def main() -> str:
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
