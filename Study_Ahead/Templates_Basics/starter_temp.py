import os
from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html')

@app.route('/puppy/<name>')
def puppy(name):
    return render_template('puppy_name.html', name=name)

@app.route('/another/<name>')
def another(name):
    letters = list(name)
    puppy_dict = {'puppy_name': name}
    return render_template('puppy_name.html', name=name, mylist=letters,
                            my_dict=puppy_dict)


if __name__ == "__main__":
    app.run()
