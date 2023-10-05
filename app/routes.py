#!/usr/bin/python3

from connection import connection
from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug import Response
import mariadb

main = Blueprint('main', __name__, template_folder='app/templates')


@main.route("/add_contact", methods=['GET', 'POST'])
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

            return redirect(url_for('main.root'))
        except mariadb.Error as e:
            print(f"Error executing SQL: {e}")
            return "Error"
        finally:
            if conn:
                conn.close()


@main.route("/edit_contact/<string:id>", methods=['GET'])
def get_contact(id: int) -> str:
    conn = connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM contacts WHERE idcontact = %d', (id,))
    data = cur.fetchall()
    print(data[0])  # Debug Message

    return render_template('edit.html', contact=data[0])


@main.route("/update_contact/<string:id>", methods=['POST'])
def update_contact(id: int) -> Response | str:
    if request.method == 'POST':
        try:
            conn = connection()
            cur = conn.cursor()
            cur.callproc('updateContact', (id, request.form['fullname'], request.form['phone'], request.form['email']))
            conn.commit()  # It worksssssssssssssss
            flash("User Updated Successfully")

            return redirect(url_for('main.root'))
        except mariadb.Error as e:
            print(f"Error executing SQL: {e}")
            return "Error"
        finally:
            if conn:
                conn.close()


@main.route("/delete_contact/<string:id>")
def delete_contact(id: int) -> Response:
    conn = connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM contacts WHERE idcontact = {0}'.format(id))
    conn.commit()
    flash("User Removed Successfully")

    return redirect(url_for('main.root'))


@main.route("/")
def root() -> str:
    conn = connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts")
    data = cur.fetchall()

    return render_template('index.html', contacts=data)
