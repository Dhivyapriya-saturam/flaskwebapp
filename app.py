from flask import Flask, render_template
from flask import request
import csv

app = Flask(__name__, template_folder='templates')
app.config["DEBUG"] = True


@app.route('/')
def home():
    """
    Get user details for the current user
    :return:
    """
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def api():
    """
    Store user details into a csv file

    :return:
    """
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        fieldnames = ['name', 'email']

        with open('list.csv', 'w') as inFile:
            writer = csv.DictWriter(inFile, fieldnames=fieldnames)
            writer.writerow({'name': name, 'email': email})
    return 'Thanks for your input!'


@app.route('/login')
def login():
    """
    Get login details from the new user
    :return:
    """
    return render_template("login.html")


@app.route('/login/check', methods=['GET', 'POST'])
def logged():
    """
    Check the new user details with the stored csv file
    :return:
    """
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        details = [name, email]
        with open('list.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                if row == details:
                    return 'User found!'
                else:
                    return 'User not found!'


if __name__ == '__main__':
    app.run()
