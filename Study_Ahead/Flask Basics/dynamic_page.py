from flask import Flask

app = Flask(__name__)

@app.route ('/')
def index():
    return '<h1>This is a happy puppy!</h1>'

@app.route('/info')
def info():
    return '<h2>This is information!</h2>'

@app.route('/puppy/<name>')
def puppy(name):
    return '<h3>This page is for {}</h3>'.format(name)
    #this is like on a Lambda dashboard

if __name__ == '__main__':
    app.run()
