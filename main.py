from flask import Flask, render_template, jsonify, request
from datetime import datetime
import database

app = Flask(__name__)

@app.route('/')
def hello_world():
  ms_num = datetime.now().microsecond
  return render_template('index.html', ms_num=ms_num)

@app.route('/api/events')
def api_events():
  return jsonify(database.list())

@app.route('/api/events/<event_id>', methods=['DELETE'])
def api_events_delete(event_id):
  database.delete(event_id)
  return ""

@app.route('/api/events', methods=['POST'])
def api_events_create():
  location = request.json['location']
  storedEvent = database.add(location)
  return jsonify(storedEvent), 201

if __name__ == '__main__':
  database.clear()

  # Initial last seen events
  database.add('Fenway Park')
  database.add('Faneuil Hall')
  database.add('Google Cambridge Office')

  
  app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

  app.run(host='0.0.0.0', port=8080, debug=True, extra_files=['templates/index.html', 'static/css/styles.css', 'static/js/main.js', 'static/img/delete.png'])