#!/usr/bin/env python3

from app import app
from routes import main
import sys

app.register_blueprint(main)


if __name__ == '__main__':
    app.run(debug=True)
    sys.exit(0)


