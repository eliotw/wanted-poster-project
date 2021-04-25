from replit import db

idCounter = 1

# Adds an event
def add(event_location):
  id = get_id()
  event = {
    "id": id,
    "location": event_location
  }
  db.set(id, event)
  return event

# Deletes an event by id
def delete(event_id):
  del db[event_id]

# Returns a list of events
def list():
  values = db.values();
  events = [value.value for value in values]
  return events

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