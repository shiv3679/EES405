from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, EES405!"

if __name__ == '__main__':
    app.run(debug=True)

from flask import redirect

@app.route('/reports')
def reports():
    return redirect("http://externalwebsite.com/reports", code=302)

@app.route('/slides')
def slides():
    return redirect("http://externalwebsite.com/slides", code=302)

@app.route('/codes')
def codes():
    return redirect("http://externalwebsite.com/codes", code=302)
