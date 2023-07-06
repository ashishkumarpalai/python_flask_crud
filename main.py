from flask import Flask, render_template, request, redirect

app = Flask(__name__)
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
    app.run(debug=True)
