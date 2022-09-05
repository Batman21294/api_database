from flask import Flask, request, jsonify
import mysql.connector as conn

app = Flask(__name__)

mydb = conn.connect(host='localhost', user='root', passwd = 'Snape1993')
cursor = mydb.cursor()

@app.route('/mysql/search', methods=['GET'])
def search_table():
    database_name = request.args.get('database_name')
    table_name = request.args.get('table_name')

    cursor.execute('select * from {}.{}'.format(database_name,table_name))

    return jsonify(cursor.fetchall())

if __name__ == '__main__':
    app.run(port=5003)