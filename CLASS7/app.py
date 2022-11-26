from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

app = Flask(__name__)  # important

filename = 'static/finalized_model.sav'  #set current working directory to avoid error
ml_service = pickle.load(open(filename, 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/model', methods=['post'])
def model():
    height = np.int64(request.form['height'])
    result1 = ml_service.predict([[height]])
    return f"""
            <h1>Your predicted Weight 
                 <label style='color:red'>
                 {result1[0]}
                 </label>
            </h1>
            """
if __name__=='__main__':
    app.run(debug=True)