from flask import Flask, redirect, url_for

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

@app.route('/secret')
def secrete_msg():
    return "This is secret page, so welcome!"

### Building URL Dynamically

@app.route('/success/<int:score>') # using url rules
def success(score):
    html = """
            <html>
                <body>
                <h1>The Result is passed </h1>
                <br>
                <h3>You do not need to study anymore</h3>
                </body>
            </html>
            """
    return html

@app.route('/fail/<int:score>')
def fail(score):
    return 'The Person has failed and the mark is ' + str(score)

@app.route('/results/<int:marks>')
def results(marks):
    result=''
    if marks > 70:
        result='success'
    else:
        result='fail'
    return redirect(url_for(result, score=marks)) # this redirext works from the root url



if __name__ == '__main__':
    app.run(debug=True, port=5001) # debug allows you to update more easily when the page is refreshed