from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/qt')
def qt():
    return render_template('qt.html')

@app.route('/teach')
def teach():
    return render_template('teach.html')

@app.route('/cv')
def cv():
    return render_template('cv.html')

if __name__ == '__main__':
    app.run(debug=True)