import os
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

app.debug = True
data = {}

@app.route('/')
def home():
    return render_template('index.html', data=data)

@app.route('/create', methods=['POST'])
def create():
    key = request.form['key']
    value = request.form['value']
    data[key] = value
    return redirect('/')

@app.route('/update', methods=['POST'])
def update():
    key = request.form['key']
    value = request.form['value']
    if key in data:
        data[key] = value
    return redirect('/')

@app.route('/delete', methods=['POST'])
def delete():
    key = request.form['key']
    if key in data:
        del data[key]
    return redirect('/')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)