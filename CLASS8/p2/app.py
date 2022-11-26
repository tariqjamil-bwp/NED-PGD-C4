from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Thankou</h1>'
    
@app.route('/about')
def about():
    return '''
    <h1>NED University</h1><br>
    <h2>ML PGD Program</h2>
    '''
    

app.run(debug=True)

