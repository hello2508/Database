from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

# Configure db
db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

# instantiate an object for MySQL
mysql = MySQL(app)

# GET request- display orm to the user
# POSt request - store details onto the database
@app.route("/", methods=['GET','POST'])
def index():
	if request.method == 'POST':
		# Fetch form data
		userDetails = request.form
		name = userDetails['name']
		book_title = userDetails['book_title']
		review = userDetails['review']
		cur = mysql.connection.cursor()
		cur.execute("INSERT INTO test(reviewerName,booktitle,reviewText) VALUES(%s, %s, %s)",(name,book_title,review) )
		# Save changes into the database
		mysql.connection.commit()
		cur.close()
		return 'success'
	return render_template('home.html')


if __name__ == "__main__":
	app.run(debug=True)