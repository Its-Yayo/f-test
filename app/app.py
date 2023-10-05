#!/usr/bin/python3

from flask import Flask
import os


app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = os.getenv('DB_SECRET_KEY')
