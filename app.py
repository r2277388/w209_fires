from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/viz1")
def viz1():
    return render_template('viz1.html')

@app.route("/viz2")
def viz2():
    return render_template('viz2.html')

@app.route("/viz3")
def viz3():
    return render_template('viz3.html')

@app.route("/viz4")
def viz4():
    return render_template('viz4.html')

@app.route("/firepic")
def fire():
    return render_template('fire.html')

if __name__ == '__main__':
    app.run(debug=True)