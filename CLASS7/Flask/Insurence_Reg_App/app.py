from flask import Flask, request
import numpy as np
import pandas as pd
from pycaret.regression import *
import os

model_path = '/media/tjamil/work/MyPGD/CLASS7/Flask/Insurence_Reg_App'
model_file = os.path.join(model_path, 'my_best_pipeline')
loaded_model = load_model(model_file)

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <form action="/model" method='post'>
    <h1>Insurance AI Prediction Model</h1>

    <label>Age:</label> <input type='text' name='age'><br>
    <label>Gender:</label> <input type='text' name='sex'><br>
    <label>BMI:</label> <input type='text' name='bmi'><br>
    <label>Children:</label> <input type='text' name='children'><br>
    <label>Smoker:</label> <input type='text' name='smoker'><br>
    <label>Region:</label> <input type='text' name='region'><br>

    <input type='submit' value='Predict Now'>
     
    </form>
    """
    
@app.route("/model", methods=['POST'])
def about():
    age = np.int64(request.form['age'])
    sex = request.form['sex']
    bmi = np.float(request.form['bmi'])
    children = np.int64(request.form['children'])
    smoker = request.form['smoker']
    region = request.form['region']

    df = pd.DataFrame([[age, sex, bmi, children, smoker, region, None]], 
    columns=['age', 'sex', 'bmi', 'children', 'smoker', 'region', 'charges'])
    print(df)

    df1 = predict_model(loaded_model,df)
    result = df1['Label'].values[0]

    return f"""
    Client age {age}<br>
    Client sex {sex}<br>
    Client BMI {bmi}<br>
    Client children {children}<br>
    Client smoker {smoker}<br>
    Client region {region}<br>
    Client age {age}
    <h1>Predict Charges {result}</h1>
    """

app.run(debug=True)