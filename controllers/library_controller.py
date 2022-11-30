from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.books import Books

books_blueprint = Blueprint("books", __name__)

