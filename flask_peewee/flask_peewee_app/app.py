'''
    Credit for this code belongs with:
    youtube account: CS50
    title: Python Web Apps with Flask by Ezra Zigmond
    url: https://www.youtube.com/watch?v=qla-KaMF-2Q

'''



from flask import Flask, render_template, request, redirect, url_for
from models import *

app = Flask(__name__)

@app.before_request
def before_request():
    # create db if needed and connect
    initialize_db()

@app.teardown_request
def teardown_request(exception):
    # close the db connection
    db.close()

@app.route('/')
def home():
    # render the home page with the saved posts
    return render_template('home.html', posts=Post.select().order_by(Post.date.desc()))

@app.route('/new_post')
def new_post():
    return render_template('new_post.html')

@app.route('/create/', methods=['POST'])
def create_post():
    # creates new post
    Post.create(
        title=request.form['title'],
        text=request.form['text']
    )

    # return the user to the home page
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
