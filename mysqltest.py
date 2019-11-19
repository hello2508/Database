from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] ='localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'sakila' # database name

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def Home():
	# creating mysql connection
	cur = mysql.connection.cursor()
	cur.execute("SELECT * FROM sakila.actor.first_name") # execute query
	fetchdata = cur.fetchall() # fetch data from 'user' table
	cur.close()
	return render_tamplate('home.html', data = fetchdata)

def main():
	if request.method == "POST":
		details = request.form
		firstName = details['fname'] # fetches value in html form
		lastName = details['lname']
		# establish connection
		cur = mysql.connection.cursor()
		# execution of query
		cur.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (firstName,lastName))
		mysql.connection.commit()
		# close connection
		cur.close()
		return 'success'
	return render_template('home.html')


if __name__ == "__main__":
	app.run(debug=True)