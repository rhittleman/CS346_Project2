from flask import Flask, render_template, redirect, url_for, request
import db_current_for_user
import psycopg2

app = Flask(__name__)

@app.route("/game", methods=['GET', 'POST'])
def game():
    x = 0
    y = 0
    if request.method == 'POST':
        value = request.form['name']
        conn = psycopg2.connect(host="cs346proj2db.ctkh18zy1p4k.us-east-1.rds.amazonaws.com", dbname="cs346proj2db", user="cs346proj2admin", password="proj2pass")
        get = "select * from rounds"
        get2 = "select * from games"
        cursor = conn.cursor()
        cursor.execute(get)
        cursor.execute(get2)
        data = cursor.fetchall()
        data2 =cursor.fetchall()
        insert = """ INSERT INTO 'rounds'
        ('round_id', 'prev_round', 'p1-choise', 'p2-choice') VALUES
        (None, None, value, data[3]) """
        
        
        if data[3] != None:
            if data[3] == 1 and value == 1:
                return render_template('game.html', data2[2], data2[4])
            elif data[3] == 2 and value == 2:
                return render_template('game.html', data2[2], data2[4])
            elif data[3] == 3 and value == 3:
                return render_template('game.html', data2[2], data2[4])
            elif data[3] == 4 and value == 4:
                return render_template('game.html', data2[2], data2[4])
            elif data[3] == 5 and value == 5:
                return render_template('game.html', data2[2], data2[4])
            elif data[3] == 1 and (value == 2 or value == 4):
                insert = """ INSERT INTO 'games'
                ('round_id', 'prev_round', 'p1-choise', 'p2-choice') VALUES
                (None, None, data2[2]+1, None, data2[4], None) """
                cursor = conn.cursor()
                result  = cursor.execute(insert)
                conn.commit()
                return render_template('game.html', x=data2[2]+1, y=data2[4])
            elif data[3] == 2 and (value == 3 or value == 5):
                insert = """ INSERT INTO 'games'
                ('round_id', 'prev_round', 'p1-choise', 'p2-choice') VALUES
                (None, None, data2[2]+1, None, data2[4], None) """
                cursor = conn.cursor()
                result  = cursor.execute(insert)
                conn.commit()
                return render_template('game.html', x=data2[2]+1, y=data2[4])
            elif data[3] == 3 and (value == 1 or value == 4):
                insert = """ INSERT INTO 'games'
                ('round_id', 'prev_round', 'p1-choise', 'p2-choice') VALUES
                (None, None, data2[2]+1, None, data2[4], None) """
                cursor = conn.cursor()
                result  = cursor.execute(insert)
                conn.commit()
                return render_template('game.html', x=data2[2]+1, y=data2[4])
            elif data[3] == 4 and (value == 2 or value == 5):
                insert = """ INSERT INTO 'games'
                ('round_id', 'prev_round', 'p1-choise', 'p2-choice') VALUES
                (None, None, data2[2]+1, None, data2[4], None) """
                cursor = conn.cursor()
                result  = cursor.execute(insert)
                conn.commit()
                return render_template('game.html', x=data2[2]+1, y=data2[4])
            elif data[3] == 5 and (value == 1 or value == 3):
                insert = """ INSERT INTO 'games'
                ('round_id', 'prev_round', 'p1-choise', 'p2-choice') VALUES
                (None, None, data2[2]+1, None, data2[4], None) """
                cursor = conn.cursor()
                result  = cursor.execute(insert)
                conn.commit()
                return render_template('game.html', x=data2[2]+1, y=data2[4])
            else:
                insert = """ INSERT INTO 'games'
                ('round_id', 'prev_round', 'p1-choise', 'p2-choice') VALUES
                (None, None, data2[2], None, data2[4]+1, None) """
                cursor = conn.cursor()
                result  = cursor.execute(insert)
                conn.commit()
                return render_template('game.html', x=data2[2], y=data2[4]+1)

    return render_template('game.html', x=x, y=y)

@app.route("/", methods=['GET', 'POST'])
def main():
    error = None
    if request.method == 'POST':
        curr = db_current_for_user.find_user(request.form['username'], request.form['password'])
        if None != curr:
            return redirect(url_for('game'))
        error = 'Invalid Credentials. Please try again.'
    return render_template('index.html', error=error)

if __name__== "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
