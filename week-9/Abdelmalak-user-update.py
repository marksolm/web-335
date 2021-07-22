# /*
# ;============================================
# ; Title: Exercise 9.3
# ; Author: Professor Krasso
# ; Date: 21 July 2021
# ; Modified By: Soliman Abdelmalak
# ; Description: Updating and Deleting Documents
# ;===========================================
# */

#// import statements
from pymongo import MongoClient
import pprint
import datetime
#// connect to local MongoDB instance
client = MongoClient('localhost', 27017)
db = client.web335
#// update a user document
db.users.update_one(
    {"employee_id": "0000100"},
    {
        "$set": {
            "email": "sabdelmalak@@my365.bellevue.edu"
        }
    }
)
# Find and print the specified document.
pprint.pprint(db.users.find_one({"employee_id": "0000100"}))