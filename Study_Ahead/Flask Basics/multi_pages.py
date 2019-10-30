from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello, Puppy!</h1>'

@app.route('/info')
def info():
    return '<h2>This is the second page</h2>'

if __name__ == "__main__":
    app.run()
