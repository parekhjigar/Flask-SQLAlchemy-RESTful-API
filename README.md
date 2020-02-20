# Flask SQLAlchemy RESTful API

A database driven RESTful JSON API in Python with Flask-RESTful and ORM SQLAlchemy.

## Installing virtualenv

	`$ pip install virtualenv`
	

### Creating a virtual environment

Set the current working directory to the new project directory and run the following command. It creates a virtual environment named venv.

	`$ virtualenv venv`
	
### Activating the venv

	`$ source venv/bin/activate`
	
### Installing Flask-Marshmallow

Flask-Marshmallow is a thin integration layer for Flask and marshmallow (an object serialization/deserialization library) which integrates with Flask-SQLAlchemy to serialize a collection of objects of SQLAlchemy data rows into textual representation, in this case to JSON.

	`pip install flask-marshmallow`