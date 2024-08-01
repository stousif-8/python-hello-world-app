from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World setup created using Docker by Syed Tousif'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

