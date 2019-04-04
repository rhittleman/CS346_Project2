from flask import Flask, render_template, redirect, url_for, request
import db_current_for_user
import psycopg2

app = Flask(__name__)

@app.route("/game", methods=['GET', 'POST'])
def game():
    x = 0
    y = 0
    if request.method == 'POST':
        option = request.form['options']
        conn = psycopg2.connect(host="cs346proj2db.ctkh18zy1p4k.us-east-1.rds.amazonaws.com", dbname="cs346proj2db", user="cs346proj2admin", password="proj2pass")
        get = "SELECT * FROM rounds"
        get2 = "SELECT * FROM games"
        
        cursor = conn.cursor()
        cursor.execute(get)
        data = cursor.fetchall()
        
        cursor = conn.cursor()
        cursor.execute(get2)
        data2 = cursor.fetchall()
        value = 0
        if option == "r":
            value = 1
        elif option == "p":
            value = 2
        elif option == "s":
            value = 3
        elif option == "sp":
            value = 4
        elif option == "l":
            value = 5
        insert = """ INSERT INTO rounds
        (prev_round, p1_choice, p2_choice) VALUES
        (%s, %s, %s) """
        rtuple = (None, value, data[3])
        cursor = conn.cursor()
        result  = cursor.execute(insert, rtuple)
        conn.commit()
        
        if data[3] != None:
            if data[3] == 1 and value == 1:
                cursor.close()
                conn.close()
                return render_template('game.html', x=data2[2], y=data2[4])
            elif data[3] == 2 and value == 2:
                cursor.close()
                conn.close()
                return render_template('game.html', x=data2[2], y=data2[4])
            elif data[3] == 3 and value == 3:
                cursor.close()
                conn.close()
                return render_template('game.html', x=data2[2], y=data2[4])
            elif data[3] == 4 and value == 4:
                cursor.close()
                conn.close()
                return render_template('game.html', x=data2[2], y=data2[4])
            elif data[3] == 5 and rvalue == 5:
                cursor.close()
                conn.close()
                return render_template('game.html', x=data2[2], y=data2[4])
            elif data[3] == 1 and (value == 2 or value == 4):
                insert = """ INSERT INTO games
                (current_round, p1_score, p1_done, p2_score, p2_done) VALUES
                (%s, %s, %s, %s, %s) """
                gtuple = (None, data2[2]+1, False, data2[4], False)
                cursor = conn.cursor()
                result  = cursor.execute(insert, gtuple)
                conn.commit()
                cursor.close()
                conn.close()
                return render_template('game.html', x=data2[2]+1, y=data2[4])
            elif data[3] == 2 and (value == 3 or value == 5):
                insert = """ INSERT INTO games
                (current_round, p1_score, p1_done, p2_score, p2_done) VALUES
                (%s, %s, %s, %s, %s) """
                gtuple = (None, data2[2]+1, False, data2[4], False)
                cursor = conn.cursor()
                result  = cursor.execute(insert, gtuple)
                conn.commit()
                cursor.close()
                conn.close()
                return render_template('game.html', x=data2[2]+1, y=data2[4])
            elif data[3] == 3 and (value == 1 or value == 4):
                insert = """ INSERT INTO games
                (current_round, p1_score, p1_done, p2_score, p2_done) VALUES
                (%s, %s, %s, %s, %s) """
                gtuple = (None, data2[2]+1, False, data2[4], False)
                cursor = conn.cursor()
                result  = cursor.execute(insert, gtuple)
                conn.commit()
                cursor.close()
                conn.close()
                return render_template('game.html', x=data2[2]+1, y=data2[4])
            elif data[3] == 4 and (value == 2 or value == 5):
                insert = """ INSERT INTO games
                (current_round, p1_score, p1_done, p2_score, p2_done) VALUES
                (%s, %s, %s, %s, %s) """
                gtuple = (None, data2[2]+1, False, data2[4], False)
                cursor = conn.cursor()
                result  = cursor.execute(insert, gtuple)
                conn.commit()
                cursor.close()
                conn.close()
                return render_template('game.html', x=data2[2]+1, y=data2[4])
            elif data[3] == 5 and (value == 1 or value == 3):
                insert = """ INSERT INTO games
                (current_round, p1_score, p1_done, p2_score, p2_done) VALUES
                (%s, %s, %s, %s, %s) """
                gtuple = (None, data2[2]+1, False, data2[4], False)
                cursor = conn.cursor()
                result  = cursor.execute(insert, gtuple)
                conn.commit()
                cursor.close()
                conn.close()
                return render_template('game.html', x=data2[2]+1, y=data2[4])
            else:
               insert = """ INSERT INTO games
               (current_round, p1_score, p1_done, p2_score, p2_done) VALUES
               (%s, %s, %s, %s, %s) """
               gtuple = (None, data2[2], False, data2[4]+1, False)
               cursor = conn.cursor()
               result  = cursor.execute(insert, gtuple)
               conn.commit()
               cursor.close()
               conn.close()
               return render_template('game.html', x=data2[2], y=data2[4]+1)
        else:
            return render_template('game.html', x=data2[2], y=data2[4])
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
