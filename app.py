from flask import Flask, render_template, url_for

from flaskext.markdown import Markdown

app = Flask(__name__)
Markdown(app)

@app.route('/')
def index():
    return render_template('index.html')
    #return render_template('test.html')

@app.route('/research')
def research():
    return render_template('research.html')

@app.route('/teach')
def teach():
    return render_template('teach.html')

@app.route('/cv')
def cv():
    return render_template('cv.html')

if __name__ == '__main__':
    app.run(debug=True)

