from flask import Flask,request,redirect,render_template
from flask_bootstrap import Bootstrap

from flask_script import Manager

app=Flask(__name__)
bootstrap = Bootstrap(app)



@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    #return '<h1>Hello World! %s</h1>'% user_agent
    return redirect('https://www.google.com')

@app.route('/usr/<name>')
def user(name):
    return render_template('usr.html',name=name)



#if __name__ == '__main__':
    #app.run(debug=True)
 #   bootstrap.run()