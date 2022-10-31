from flask import Flask
app = Flask(__name__)
from lb import categories, users, notes

