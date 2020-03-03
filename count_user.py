
import sys
from db.example.user import UserDB

book_ids = sys.argv[1]
print book_ids
_db = UserDB()
count = _db.counts(book_ids=book_ids)
print count

