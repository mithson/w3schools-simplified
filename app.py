from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/html')
def html():
    return render_template('html.html')

@app.route('/css')
def css():
    return render_template('css.html')

@app.route('/js')
def js():
    return render_template('js.html')

@app.route('/sql')
def sql():
    return render_template('sql.html')

@app.route('/python')
def python():
    return render_template('python.html')

@app.route('/javascript')
def javascript():
    return redirect(url_for('js'))

if __name__ == '__main__':
    app.run(port=8000)
