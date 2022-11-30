from db.run_sql import run_sql

from models.authors import Authors
from models.books import Books
import repositories.books_repository as book_repository
import repositories.authors_repository as authors_repository

def save(author):
    sql = "INSERT INTO authors (name) VALUES (%s) RETURNING *"
    values = [author.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    author.id = id
    return author

def select_all():
    authors = []

    sql = "SELECT * FROM authors"
    results = run_sql(sql)

    for row in results:
        author = Authors(row['author_name'], row['id'])
        authors.append(author)
    return authors

def select(id):
    author = None
    sql = "SELECT * FROM authors WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        author = Authors(result['author_name'], result['id'] )
    return author

def delete_all():
    sql = "DELETE FROM authors"
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM authors WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(author):
    sql = "UPDATE authors SET (author_name) = (%s) WHERE id = %s"
    values = [author.author_name, author.id]
    run_sql(sql, values)

def authors(author):
    tasks = []

    sql = "SELECT * FROM auhtors WHERE auhtor_id = %s"
    values = [author.id]
    results = run_sql(sql, values)

    for row in results:
        author = Authors(row['author_name'], row['author_id'])
        tasks.append(author)
    return author
