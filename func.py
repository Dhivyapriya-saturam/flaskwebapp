import csv

from flask import render_template
from flask import request


def home():
    """
    Get the user details for the current user
    :return:
    """
    return render_template('home.html')


def api():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        fieldnames = ['name', 'email']

        with open('list.csv', 'w') as inFile:
            writer = csv.DictWriter(inFile, fieldnames=fieldnames)
            writer.writerow({'name': name, 'email': email})
    return 'Thanks for your input!'


def login():
    return render_template("login.html")


def signin():
    """

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
