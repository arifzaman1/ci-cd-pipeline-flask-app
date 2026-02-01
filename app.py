from flask import Flask


app = Flask(__name__)

@app.route('/')
def home():
    return "Hello! This is a CI/CD Flask app running with docker and Jenkins."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

