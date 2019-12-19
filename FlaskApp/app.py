from flask import Flask, render_template, request, redirect
import mysql.connector
app = Flask(__name__)

db = mysql.connector.connect(
	host = '18.141.90.224',
    user = 'root',
    password = '',
    database = 'dbds',
    buffered = True
	)


@app.route("/", methods=['GET','POST'])
def index():
	cur = db.cursor()
	if request.method == 'POST':
		# Fetch form data
		userDetails = request.form

		asin = userDetails['asin']
		#helpful = userDetails['helpful']
		overall = userDetails['overall']
		review = userDetails['review']
		reviewTime= userDetails['reviewTime']
		ID = userDetails['ID']
		name = userDetails['name']
		summary = userDetails['summary']		
		unixReviewTime= userDetails ['unixReviewTime']		
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
	result = cur.execute("SELECT asin, reviewerName, reviewText, helpful FROM kindle_reviews WHERE asin='B000F83SZQ' LIMIT 10")
	bookasin = cur.fetchall()
	return render_template('home.html', bookasin=bookasin)

	# return render_template('home.html')

@app.route("/average")
def bookavg():
	cur = db.cursor();
	# cur.execute("SELECT asin, AVG(overall) FROM kindle_reviews HAVING 'count(asin)>1' GROUP BY asin LIMIT 9")
	cur.execute("SELECT asin, avg(overall) from kindle_reviews group by asin order by avg(overall) desc limit 9 ")
	average = cur.fetchall()
	return render_template('average.html', average=average)



if __name__ == "__main__":
	app.run(debug=True)
