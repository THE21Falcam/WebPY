from flask import Flask, render_template,request
import uuid

app = Flask(__name__)

@app.route('/')
def mainsite():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()
