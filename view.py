from app import app
from flask import render_template, request, redirect, url_for
from models import Employee
from app import db


@app.route('/')
def index():
    employees = Employee.query.all()
    return render_template('index.html', employees=employees)


@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        name = request.form['name']
        last_name = request.form['last_name']
        age = request.form['age']
        exp = request.form['exp']

        my_data = Employee(name, last_name, age, exp)
        db.session.add(my_data)
        db.session.commit()

        return redirect(url_for('index'))


@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        employee = Employee.query.get(request.form.get('id'))

        employee.name = request.form['name']
        employee.last_name = request.form['last_name']
        employee.age = request.form['age']
        employee.exp = request.form['exp']

        db.session.commit()

        return redirect(url_for('index'))


@app.route('/delete/<id>/', methods=['GET', 'POST'])
def delete(id):
    employee = Employee.query.get(id)
    db.session.delete(employee)
    db.session.commit()

    return redirect(url_for('index'))







