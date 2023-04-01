from flask import Flask, render_template

app = Flask(__name__)

@app.route('/html')
def index():
    return render_template('html.html')

@app.route('/css')
def about():
    return render_template('css.html')

@app.route('/js')
def contact():
    return render_template('js.html')

@app.route('/sql')
def portfolio():
    return render_template('sql.html')

@app.route('/python')
def services():
    return render_template('python.html')

if __name__ == '__main__':
    app.run()
