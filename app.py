from flask import Flask, render_template, redirect, url_for, send_file
import os

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


@app.route('/bootstrap')
def bootstrap():
    return render_template('bootstrap.html')

@app.route('/mongodb')
def mongodb():
    return render_template('mongodb.html')

@app.route('/javascript')
def javascript():
    return redirect(url_for('js'))

@app.route('/react')
def react():
    file_path = os.path.join(app.root_path, 'templates', 'react.html')
    return send_file(file_path, as_attachment=True)

@app.route('/django')
def django():
    file_path = os.path.join(app.root_path, 'templates', 'django.html')
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(port=8000)
