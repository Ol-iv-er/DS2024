from flask import Flask

## Skeleton of a Flask Framework

## this is WSGI (Web Server Gateway Interface) Application

app=Flask(__name__)

## Decorator -> Functions under this are triggered when that web page is visited
@app.route('/') #first parameter 'rule' is like the URL
def welcome():
    return 'Welcome to my first Flask App. This is kinda COOL!'

@app.route('/cool') #first parameter 'rule' is like the URL
def cool():
    return 'Welcome special people to the next page'

if __name__ == '__main__':
    app.run(debug=True) # debug allows you to update more easily when the page is refreshed