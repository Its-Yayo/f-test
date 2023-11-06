#!/usr/bin/env python3

from dotenv import load_dotenv
import mariadb
import os
import sys

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
