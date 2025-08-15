from flask import Flask, render_template, jsonify
app=Flask(__name__)
@app.route("/")
def index():
    return "<h1>Hey</h1>"
if __name__=='__main__':
    app.run(host="0.0.0.0",port=8001)