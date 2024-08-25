### Integrate HTML with FLask (Jinja2 Techniques: seperate data source you can integrate with HTML)
### HTTP verb GET and POST

## Jinja2 template
'''
{%...%} any conditions, for loops and statements
{{ output }} expression to print output variable
{#...#} this is for comments for html code but does not show on the web page
'''
from flask import Flask, redirect, url_for, render_template, request


app=Flask(__name__)

@app.route('/') 
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>') 
def success(score):

    return render_template("results.html", result = score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The Person has failed and the marks is " + str(score)
    #return render_template()

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
@app.route('/submit', methods =['POST', 'GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        datascience = float(request.form['datascience'])
        total_score = (science + maths + c + datascience)/4
    
    return redirect(url_for("success", score = total_score))


if __name__ == '__main__':
    app.run(debug=True) 