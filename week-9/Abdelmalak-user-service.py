# /*
# ;============================================
# ; Title: Exercise 9.2
# ; Author: Professor Krasso
# ; Date: 20 July 2021
# ; Modified By: Soliman Abdelmalak
# ; Description: Querying and Creating Documents
# ;===========================================
# */

#// import statements
from pymongo import MongoClient
import pprint
import datetime

#// connect to local MongoDB instance
client = MongoClient('localhost', 27017)

db = client.web335

#// Create a new user document
user = {
  "first_name": "Soliman",
  "last_name": "Abdelmalak",
  "email": "elmalak@email.com",
  "employee_id": "0000100",
  "date_created": datetime.datetime.utcnow()
}

# Insert a new user document.
user_id = db.users.insert_one(user).inserted_id

# Output the auto-generated user_id.
print(user_id)

employee_id = "0000100"

# Find and print the specified document.
pprint.pprint(db.users.find_one({"employee_id": employee_id}))