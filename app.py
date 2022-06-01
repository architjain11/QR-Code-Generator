from flask import Flask, render_template, request
import pyqrcode
import png

app = Flask(__name__)

@app.route("/")
def index():
    message = 'Built by Archit'
    return render_template("index.html", message=message)

@app.route("/newQR")
def newQR():
    message = request.args.get('message')
    d = pyqrcode.create(message)
    d.png('/output.png', scale=6)
    return render_template("index.html", message=message)