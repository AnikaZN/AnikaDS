from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('stuff.html')

@app.route('/puppy/<name>')
def puppy(name):
    return render_template('puppy_name_2.html', name=name)

@app.route('/another/<name>')
def another(name):
    mylist = [name]
    my_dict = {'Name': name}
    return render_template('puppy_name_2.html', mylist=mylist, my_dict=my_dict)


if __name__ == '__main__':
    app.run()
