from flask import Flask
app=Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to my first Flask App"

if __name__ =='__main__':
    app.run()