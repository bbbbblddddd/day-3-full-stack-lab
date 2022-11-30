import pdb
from models.authors import Authors
from models.books import Books

import repositories.authors_repository as author_repository
import repositories.books_repository as books_repository

author1 = Authors("Mary Shelley")
author_repository.save(author1)

author2 = Authors("F Scott Fitzgerald")
author_repository.save(author2)

author3 = Authors("Shirley Jackson")
author_repository.save(author3)

author4 = Authors("George Orwell")
author_repository.save(author4)

book_1 = Books("Frankenstein", "Horror", 10, author1)
books_repository.save(book_1)

book_2 = Books("The Great Gatsby", "Drama", 12, author2)
books_repository.save(book_2)

book_3 = Books("House on Haunted Hill", "Horror", 8, author3)
books_repository.save(book_2)

book_4 = Books("1984", "Sci Fi", 5, author4)
books_repository.save(book_2)





author_repository.select_all()


pdb.set_trace()
