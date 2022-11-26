from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Thankyou</h>'

app.run(debug=True)