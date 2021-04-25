from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
  ms_num = datetime.now().microsecond
  return render_template('index.html', ms_num=ms_num)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True, extra_files=['templates/index.html', 'static/css/styles.css', 'static/js/main.js', 'static/img/delete.png'])