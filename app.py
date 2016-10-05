#!/home/raphaeliarussi/.pythonbrew/venvs/Python-2.7.10/flask-env/bin/python
from flask import request, url_for, jsonify
from flask.ext.api import FlaskAPI, exceptions, status
import MySQLdb

db = MySQLdb.connect('localhost','root','29367253','api')

app = FlaskAPI(__name__)

@app.route('/api/v.1.0/users',methods=['GET'])
def fetch_all_users():
    """ API version 1.0
    Return all users param GET
    """
    cursor = db.cursor()
    cursor.execute("SELECT * FROM user")
    data = cursor.fetchall()
    return {'users':data}


@app.route('/api/v.1.0/user/<int:id>',methods=['GET'])
def fetch_one_user(id):
    """ API version 1.0
    Return one user param GET
    """
    # id = request.args.get('id')
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM user
          WHERE id = %s""", (id,))
    data = cursor.fetchall()
    if len(data) > 0:
        content = {'data': 'not rows found'}
        return content, status.HTTP_204_NO_CONTENT
    else:
        return {'user': data}



if __name__ == '__main__':
    app.run(debug=True)
