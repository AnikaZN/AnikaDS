from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    puppies = ['Tyler', 'Anika', 'Rudy']
    return render_template('control_flow.html', puppies=puppies)

@app.route('/zoo')
def animals():
    animals = {'dog': 'Felix', 'cat': 'Lucy', 'bird': 'Pedro'}
    return render_template('control_flow_dict.html', animals=animals)

#create a webpage/write a script that poses a question
#then you write a SQL query and get an answer

if __name__ == '__main__':
    app.run()
