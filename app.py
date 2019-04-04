from flask import Flask, render_template, redirect, url_for, request
import db_current_for_user

app = Flask(__name__)

@app.route("/game")
def game():
    return render_template('game.html')

@app.route("/", methods=['GET', 'POST'])
def main():
    error = None
    if request.method == 'POST':
        curr = db_current_for_user.find_user(request.form['username'], request.form['password'])
        if None != curr
            return redirect(url_for('game'))
        error = 'Invalid Credentials. Please try again.'
    return render_template('index.html', error=error)

if __name__== "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
