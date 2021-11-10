from flask import Flask, session, render_template, redirect, request

app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        credentials_username = request.form['username']
        credentials_password = request.form['password']
        credentials_filename = "credentials.txt"
        credentials_file = open(credentials_filename, "a")
        credentials_file.write(str(credentials_username) + ', ' + str(credentials_password) + ', ')
        credentials_file.close()

    return render_template("register.html")

app.run(debug=True)
