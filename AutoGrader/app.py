from compile import compilee
import os
import subprocess
from flask import Flask, render_template, request
from werkzeug import secure_filename
app = Flask(__name__)

@app.route('/')
def upload_file():
   return render_template('upload.html')

app.config['upload_dir'] = './uploads/'
@app.route('/', methods = ['GET', 'POST'])
def upload_file_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(os.path.join(secure_filename(f.filename)))
      result = compilee()
      return result
     #return 'uploaded successfully'

if __name__ == '__main__':
   app.run(host="0.0.0.0", debug=True)


