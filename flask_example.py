from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello'

@app.route('/1')
def testpage1():
    return "page 1 ok"

@app.route('/2')
def testpage2():
    return "page 2 ok"

def main():
    app.run(debug  = True, port = 8080)

if __name__ == '__main__':
    main()