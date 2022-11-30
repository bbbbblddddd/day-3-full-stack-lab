import pdb
from models.authors import Authors
from models.books import Books

import repositories.authors_repository as author_repository
# import repositories.books_repository as books_repository

author1 = Authors("Mary Shelley")
author_repository.save(author1)

author2 = Authors("F Scott Fitzgerald")
author_repository.save(author2)

author3 = Authors("Shirley Jackson")
author_repository.save(author3)

author4 = Authors("George Orwell")
author_repository.save(author4)

author_repository.select_all()


pdb.set_trace()
