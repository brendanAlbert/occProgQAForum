
''' step 2: import SQLAlchemy class from module '''

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, flash, url_for, redirect, render_template

'''
    step 3: create a Flask application object and set
    URI for the database to be used. And set secret token.

'''
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "Science rules!"


'''
    step 4: create an object of SQLAlchemy class with
    application object as the parameter. This object
    contains helper functions for ORM
    (Object Relational Mapping) operations.

    Also provides a parent Model class using which user
    defined models are declared. Below, a students model
    is created.

'''

db = SQLAlchemy(app)
class students(db.Model):
    id = db.Column('student_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10))

    def __init__(self, name, city, addr, pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin

'''
    step 5: To create / use database mentioned in URI,
    run the create_all() method.

    You can apply a filter to the retrieved record set
    by using the filter attribute. For instance, in
    order to retrieve records with city = 'Costa Mesa'
    in students table, use following statement:

    Students.query.filter_by(city = 'Costa Mesa').all()
'''

db.create_all()


'''
    Step 6: The entry point of the app is the show_all()
    function bound to the '/' URL.

    The record set of students table is sent as a parameter
    to the HTML template.

    The server side code in the template renders the
    records in HTML table form.
'''

@app.route('/')
def show_all():
    return render_template('show_all.html', students = students.query.all() )


@app.route('/new', methods = ['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['city'] or not request.form['addr']:
            flash('Please enter all the fields', 'error')
        else:
            student = students(request.form['name'], request.form['city'],request.form['addr'], request.form['pin'])

            db.session.add(student)
            db.session.commit()

            flash('Record successfully added!')
            return redirect(url_for('show_all'))

    return render_template('new.html')


if __name__ == '__main__':
    db.create_all()
    app.run(debug = True)
