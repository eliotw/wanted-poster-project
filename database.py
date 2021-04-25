from replit import db

idCounter = 1

# Add a record
def add(location):
  id = get_id()
  record = {
    "id": id,
    "location": location
  }
  db.set(id, record)
  return record

# Deletes an record by id
def delete(record_id):
  del db[record_id]

# Returns a list of records
def list():
  values = db.values();
  records = [value.value for value in values]
  return records

def clear():
  keys = db.keys()
  for key in keys:
    del db[key]

# Helper method to get auto-incrementing id
def get_id():
  global idCounter
  id = idCounter;
  idCounter += 1
  return id