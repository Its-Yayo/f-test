#!/usr/bin/python3

from flask import Flask, render_template, request, redirect, url_for, flash, session
from dotenv import load_dotenv
from werkzeug import Response
import mariadb
import sys
import os

app = Flask(__name__)
load_dotenv()

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = os.getenv('DB_SECRET_KEY')


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


@app.route("/add_contact", methods=['POST'])
def add_user() -> Response | str:
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']

        try:
            conn = connection()
            cur = conn.cursor()
            cur.callproc('insertContact', (fullname, phone, email))
            conn.commit()
            flash("User Added Successfully")
            return redirect(url_for('main'))
        except mariadb.Error as e:
            print(f"Error executing SQL: {e}")
            return "Error executing SQL"
        finally:
            if conn:
                conn.close()


@app.route("/edit_contact/<id>", methods=['POST'])
def get_contact(id: int) -> str:
    # FIXME: 405 Method Not Allowed
    conn = connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM contacts WHERE idcontact = %d', (id))
    data = cur.fetchall()
    print(data[0])  # Debug Message

    return render_template('edit.html', contact=data[0])


@app.route("/delete_contact/<string:id>")
def delete_contact(id: int) -> Response:
    conn = connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM contacts WHERE idcontact = {0}'.format(id))
    conn.commit()
    flash("User Removed Successfully")

    return redirect(url_for('main'))


@app.route("/")
def main() -> str:
    conn = connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts")
    data = cur.fetchall()

    return render_template('index.html', contacts=data)


if __name__ == '__main__':
    app.run()
    sys.exit(1)
