from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", x=3)

@app.route('/<y>/<x>')
def index1(x,y):
    return render_template("index.html", x=int(x),y=int(y))

@app.route('/4')
def index2():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True) 