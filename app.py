from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, Flask!'

@app.route('/hello/<name>')
def hello_name(name):
    return render_template('hello.html', name='jiji')

if __name__ == '__main__':
    app.run(debug=True)

