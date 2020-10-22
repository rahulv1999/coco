from flask import Flask,render_template,send_from_directory,request,redirect
from werkzeug.utils import secure_filename
import numpy as np
import pandas as pd
import csv
import os



app = Flask(__name__)


@app.route('/')
def home():
    return render_template('upload.html')


@app.route('/upload',methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        file.save(secure_filename('data.csv'))
        return render_template('upload.html',text='file uploaded')
    
@app.route('/download')
def download():
    return send_from_directory(directory='',filename="data.csv",as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)