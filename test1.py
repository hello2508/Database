from flask import Flask, render_template, request, redirect, flash
from flask_mysqldb import MySQL
# from flask_sqlalchemy import SQLAlchemy
import MySQLdb

######
import os
#####

app = Flask(__name__)

# db configuration required by flask
app.config['MYSQL_HOST'] ='localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'sutd1234'
app.config['MYSQL_DB'] = 'dbds.kindle_reviews'

# create an instance which will provide access
mysql = MySQL(app)

@app.route("/")
def home():
	# establish connection
	cur = mysql.connection.cursor()
	cur.execute("SELECT asin FROM dbds.kindle_reviews LIMIT 10") # execute query
	# for row in cur.fetchall():
	# 	print row[1]
	# fetchdata = cur.fetchall() # fetch(one/many) data from 'dbds.kindle_reviews' table
	cur.close()

	return render_tamplate('home.html',data="nodata1")

@app.route("/test")
def test_route():
	user_details = {
		'asin':'B000F83SZQ',
		'reviewerID':'A1F6404F1VG29J'
	}
	#####
	print("current dir: {0}".format(os.getcwd()))
	####

	return render_template('home.html', user="user_details")
	# return (user_details)

# Login Page
# @app.route('/login', methods=["GET","POST"])
# def login_page():
# 	try:

# 	except Exception as e:
# 		flash(e) #display error
# 		return render_template("login.html", error=error)

# 	return render_template("login.html")

# Error handling
@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html")



if __name__ == "__main__":
	app.run(debug=True)