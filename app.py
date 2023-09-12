#!/usr/bin/python3

from flask import Flask
import mariadb
import sys
import os

app = Flask(__name__)

@app.route("/")
def main() -> str:
    return "TODO Implementation"

if __name__ == '__main__':
    app.run()
    sys.exit(1)

