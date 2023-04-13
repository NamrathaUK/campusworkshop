"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrq3jfdvk4rjsv9dqmg-a.oregon-postgres.render.com",
        database="todo_v9yu",
        user="root",
        password="dTKzv3iqzBPXNE9ZyMTWSYMkdupcB6Xx")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
