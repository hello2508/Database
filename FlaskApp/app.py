from flask import Flask, render_template, request, redirect
import mysql.connector
app = Flask(__name__)

db = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	password = 'sutd1234',
	database = 'dbds'
	)


@app.route("/", methods=['GET','POST'])
def index():
	if request.method == 'POST':
		# Fetch form data
		userDetails = request.form

		asin = userDetails['asin']
		# helpful = '[0,0]'
		overall = userDetails['overall']
		review = userDetails['review']
		reviewTime= userDetails['reviewTime']
		ID = userDetails['ID']
		name = userDetails['name']
		summary = userDetails['summary']		
		unixReviewTime= userDetails ['unixReviewTime']
		cur = db.cursor()
		# Create a database called test and create necessary tables
		# cur.execute("INSERT INTO test(reviewerName,asin,reviewText,summary,overall,reviewTime,unixReviewTime) VALUES(%s,%s,%s,%s,%s,%s,%s)"
                            # ,(name,asin,review,summary,overall,reviewTime,unixReviewTime))
		cur.execute("INSERT INTO test1(asin,helpful,overall,reviewText,reviewTime,reviewerID,reviewerName,summary,unixReviewTime) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                            ,(asin,0,overall,review,reviewTime,ID,name,summary,unixReviewTime))
		# Save changes into the database
		db.commit()
		cur.close()
		# return 'update successful'
		# return redirect('/users')
	return render_template('home.html')


if __name__ == "__main__":
	app.run(debug=True)
