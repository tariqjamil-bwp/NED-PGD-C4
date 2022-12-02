from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return 'Hello World \
        pakistan zinda bad \
        '

@app.route("/about")
def about():
    return "<h1>About</h1>\
        Pakistan Zindabad\
        we love our country\
        "

app.run(debug=True)