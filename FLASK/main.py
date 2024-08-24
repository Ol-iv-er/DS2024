### Integrate HTML with FLask (Jinja2 Techniques: seperate data source you can integrate with HTML)
### HTTP verb GET and POST

from flask import Flask, redirect, url_for, render_template


app=Flask(__name__)

@app.route('/') 
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>') 
def success(score):
    return render_template()

@app.route('/fail/<int:score>')
def fail(score):
    return render_template()

### Result Checker
@app.route('/results/<int:marks>')
def results(marks):
    result=''
    if marks > 70:
        result='success'
    else:
        result='fail'
    return redirect(url_for(result, score=marks))

### Result Checker HTML page
""" @app.route('/submit', methods =['POST', 'GET'])
def submit():
    pass """


if __name__ == '__main__':
    app.run(debug=True) 