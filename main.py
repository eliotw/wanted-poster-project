from flask import Flask, render_template, jsonify, request
from datetime import datetime
import database

app = Flask(__name__)

@app.route('/')
def hello_world():
  ms_num = datetime.now().microsecond
  return render_template('index.html', ms_num=ms_num)

@app.route('/api/records')
def api_records():
  return jsonify(database.list())

@app.route('/api/records/<record_id>', methods=['DELETE'])
def api_records_delete(record_id):
  database.delete(record_id)
  return ""

@app.route('/api/records', methods=['POST'])
def api_records_create():
  location = request.json['location']
  storedRecord = database.add(location)
  return jsonify(storedRecord), 201

if __name__ == '__main__':
  database.clear()

  # Initial last seen records
  database.add('Fenway Park')
  database.add('Faneuil Hall')
  database.add('Google Cambridge Office')

  
  app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

  app.run(host='0.0.0.0', port=8080, debug=True, extra_files=['templates/index.html', 'static/css/styles.css', 'static/js/main.js', 'static/img/delete.png'])