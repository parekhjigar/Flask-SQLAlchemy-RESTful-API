# Flask SQLAlchemy RESTful API

A database driven RESTful JSON API in Python with Flask-RESTful and ORM SQLAlchemy.

## Installing virtualenv

	`$ pip install virtualenv`
	

### Creating a virtual environment

Set the current working directory to the new project directory and run the following command. It creates a virtual environment named venv.

	`$ virtualenv venv`
	
### Activating the venv

	`$ source venv/bin/activate`
	
## Installing Flask-Marshmallow

Flask-Marshmallow is a thin integration layer for Flask and marshmallow (an object serialization/deserialization library) which integrates with Flask-SQLAlchemy to serialize a collection of objects of SQLAlchemy data rows into textual representation, in this case to JSON.

	`pip install flask-marshmallow`

## Installing Flask JSON Web Tokens

JSON Web Token (JWT) is an open standard that defines a compact and self-contained way for securely transmitting information between parties as a JSON object. Here it is used to build the user management system. Flask-JWT-Extended adds support for using JSON Web Tokens to Flask for protecting views by adding decorators to the routes that are to be protected.

	`pip install Flask-JWT-Extended`

## Installing Flask-Mail

A Flask extension for sending email messages. Here used to retrieve passwords.

	`pip install Flask-Mail`
