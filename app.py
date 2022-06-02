from flask import Flask, render_template, request
import pyqrcode
import png
import shutil

app = Flask(__name__)

@app.route("/")
def index():
    message = 'Built by Archit'
    return render_template("index.html", message=message)

@app.route("/newQR")
def newQR():
    message = request.args.get('message')
    d = pyqrcode.create(message)
    d.png('out.png', scale=6)
    src_path = r"out.png"
    dst_path = r"static\out.png"
    shutil.move(src_path, dst_path)
    return render_template("output.html", message=message, out='/static/out.png')