from flask import Flask, render_template, jsonify, request
from datetime import datetime
from replit import db

app = Flask(__name__)

idCounter = 3;

@app.route('/')
def hello_world():
  ms_num = datetime.now().microsecond
  return render_template('index.html',ms_num=ms_num)

@app.route('/api/events')
def api_events():
  values = db.values();
  events = [value.value for value in values]
  return jsonify(events)

@app.route('/api/events/<event_id>', methods=['DELETE'])
def api_events_delete(event_id):
  del db[event_id]
  return ""

def get_id():
  global idCounter
  id = idCounter;
  idCounter += 1
  return id

@app.route('/api/events', methods=['POST'])
def api_events_create():
  id = get_id()
  event = {
    'id': id,
    'location': request.json['location']
  }
  db.set(id, event)
  return jsonify(event), 201

if __name__ == '__main__':

  # Initial last seen events
  db.set(1, {'id': 1, 'location': 'Fenway Park'});
  db.set(2, {'id': 2, 'location': 'Faneuil Hall'});

  app.run(host='0.0.0.0', port=8080, debug=True, extra_files=['templates/index.html', 'static/css/main.css', 'static/js/main.js', 'static/img/delete.png'])