from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/test')
def test():
    return jsonify(message='Test works!')


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


if __name__ == '__main__':
    app.run()
