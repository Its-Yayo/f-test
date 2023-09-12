#!/usr/bin/python3

from flask import Flask
from dotenv import load_dotenv
import mariadb
import sys
import os

app = Flask(__name__)
load_dotenv()

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
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

@app.route("/")
def main() -> str:
    return "TODO Implementation"

if __name__ == '__main__':
    app.run()
    sys.exit(1)

