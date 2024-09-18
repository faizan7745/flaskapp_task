from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_azure():
    return "<center><h1>Hello, Azure Web Apps!<center></h1>"

if __name__ == '__main__':
    app.run()
