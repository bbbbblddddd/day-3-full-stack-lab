from db.run_sql import run_sql

from models.books import Books
from models.authors import Authors
import repositories.authors_repository as author_repository
import repositories.books_repository as book_repository



def save(book):
    sql = "INSERT INTO books (title, genre, price, author, author_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [task.description, task.user.id, task.duration, task.completed]
    results = run_sql(sql, values)
    id = results[0]['id']
    task.id = id
    return task