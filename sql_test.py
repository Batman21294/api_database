from flask import Flask, request, jsonify
import mysql.connector as conn

app = Flask(__name__)

mydb = conn.connect(host='localhost', user = 'root', passwd = 'Snape1993')
cursor = mydb.cursor()
cursor.execute("create database if not exists tasksql")
cursor.execute("create table if not exists tasksql.mysqltable(name varchar(30), number int)")

@app.route('/insert',methods=['POST'])
def insert_record():
    if request.method == 'POST':
        name = request.json['name']
        number = request.json['number']
        cursor.execute('insert into tasksql.mysqltable values (%s, %s)',(name, number))
        mydb.commit()
        return jsonify(str('successfully inserted !'))

@app.route('/update',methods = ['POST'])
def update():
    if request.method == 'POST':
        get_name = request.json['get_name']
        cursor.execute("update tasksql.mysqltable set number = number + 500 where name = %s",(get_name,))
        mydb.commit()
        return jsonify(str('updated successfully'))
            
if __name__ == '__main__':
    app.run()