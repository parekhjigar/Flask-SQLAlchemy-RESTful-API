from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float
import os
from flask_marshmallow import Marshmallow


app = Flask(__name__)

# Initializing SQLite Database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'emp.db')

# Instantiating SQLAlchemy
db = SQLAlchemy(app)

# Instantiating Marshmallow
ma = Marshmallow(app)

# CLI Command to create DB
@app.cli.command('db_create')
def db_create():
    db.create_all()
    print('Database created')


# CLI Command to drop DB
@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print('Database dropped')


# CLI Command to seed data to DB
@app.cli.command('db_seed')
def db_seed():
    emp1 = Emp(first_name='Jigar',
                     last_name='Parekh',
                     email='hello@parekhjigar.com',
                     password='P@ssword')

    emp2 = Emp(first_name='Alex',
                     last_name='Todd',
                     email='hello@toddalex.com',
                     password='P@ssword')

    emp3 = Emp(first_name='Bob',
                     last_name='Martin',
                     email='hello@martinbob.com',
                     password='P@ssword')

    db.session.add(emp1)
    db.session.add(emp2)
    db.session.add(emp3)

    dept1 = Department(dept_name='Machine Learning',
                        dept_type='Information Technology')

    dept2 = Department(dept_name='Business Intelligence',
                        dept_type='Management')

    db.session.add(dept1)
    db.session.add(dept2)
    db.session.commit()
    print('Database seeded!')


# Test Route
@app.route('/test')
def test():
    return jsonify(message='Test works!')

# Not Found Route
@app.route('/not_found')
def not_found():
    return jsonify(message='Resource not found'), 404


# Using request object to get key value
@app.route('/parameters')
def parameters():
    name = request.args.get('name')
    workexp = int(request.args.get('workexp'))
    if workexp < 5:
        return jsonify(message='Sorry ' + name + ', you are not eligible for the job!'), 401
    else:
        return jsonify(message='Welcome ' + name + ', you are eligible for the job!')


# Variable rule matching to grab things of URL itself
@app.route('/url_variables/<string:name>/<int:workexp>')
def url_variables(name: str, workexp: int):
    if workexp < 5:
        return jsonify(message='Sorry ' + name + ', you are not eligible for the job!'), 401
    else:
        return jsonify(message="Welcome " + name + ', you are eligible for the job!')

'''
# Employees Route
@app.route('/employees', methods=['GET'])
def employees():
    emps_list = Emp.query.all()
    result = emps_schema.dump(emps_list)
    return jsonify(result)
'''

# Departments Route
@app.route('/departments', methods=['GET'])
def departments():
    departments_list = Department.query.all()
    result = departments_schema.dump(departments_list)
    return jsonify(result)


# Register Route
@app.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    test = Emp.query.filter_by(email=email).first()
    if test:
        return jsonify(message = 'This email already exists!'), 409
    else:
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        password = request.form['password']
        emp = Emp(first_name=first_name, last_name=last_name, email=email, password=password)
        db.session.add(emp)
        db.session.commit()
        return jsonify(message='Employee added successfully!'), 201


# Database Models
class Emp(db.Model):
    __tablename__ = 'emp'
    emp_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)


class Department(db.Model):
    __tablename__ = 'department'
    dept_id = Column(Integer, primary_key=True)
    dept_name = Column(String)
    dept_type = Column(String)


# Database Schemas
class EmpSchema(ma.Schema):
    class Meta:
        fields = ('emp_id', 'first_name', 'last_name', 'email', 'password')


class DepartmentSchema(ma.Schema):
    class Meta:
        fields = ('dept_id', 'dept_name', 'dept_type')


# Instantiating Schemes
emp_schema = EmpSchema()
emps_schema = EmpSchema(many=True)

department_scheme = DepartmentSchema()
departments_schema = DepartmentSchema(many=True)


if __name__ == '__main__':
    app.run()
