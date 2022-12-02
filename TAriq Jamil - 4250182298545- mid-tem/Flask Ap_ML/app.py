from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import tensorflow as tf

app = Flask(__name__)  # important

filename = 'static/class_model.h5'  #set current working directory to avoid error
ml = tf.keras.models.load_model(filename)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/model', methods=['post'])
def model():
    c1 = np.float(request.form['c1'])
    g = request.form['g']
    c2 = np.float(request.form['c2'])
    c3 = np.float(request.form['c3'])
    c4 = np.float(request.form['c4'])
    c5 = np.float(request.form['c5'])
    c6 = np.float(request.form['c6'])
    c7 = np.float(request.form['c7'])
    c8 = np.float(request.form['c8'])
    c9 = np.float(request.form['c9'])
    c10 = np.float(request.form['c10'])
    
    if g=='M':
        c11 = 1
        c12 = 0
    else:
        c11 = 0
        c12 = 1

    labels = ['A', 'B', 'C', 'D']
    result = labels[np.argmax(ml.predict([[c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12]]))]
   
    return f"""
            <h1>Your predicted Resk Class 
                 <label style='color:red'>
                 {result[0]}
                 </label>
            </h1>
            """
if __name__=='__main__':
    app.run(debug=True)
