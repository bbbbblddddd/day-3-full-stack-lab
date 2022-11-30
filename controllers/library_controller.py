from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.books import Books
from models.authors import Authors

books_blueprint = Blueprint("books", __name__)
# authors_blueprint = Blueprint("authors", __name__)


