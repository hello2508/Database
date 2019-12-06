from flask import Flask, render_template, jsonify, url_for, request, redirect
# from flask_pymongo import PyMongo
from pymongo import MongoClient
from bson.json_util import dumps
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)  #creates an app

### Kenneth's EC2 instance
# mongo_store = MongoClient("mongodb://18.141.0.98/")
# metadata = mongo_store.goodread.metadata

### My own local
# mongo_store = MongoClient("mongodb://localhost:27017")
# metadata = mongo_store.nezukodb.metadata
# logs = mongo_store.nezukodb.logs
# logs = mongo_store.logs

#### mysql side
# Configure db
db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

# instantiate an object for MySQL
mysql = MySQL(app)

### My own local
# mongo_store = MongoClient("mongodb://localhost:27017")
# metadata = mongo_store.db.metadata
# logs = mongo_store.nezukodb.logs
# logs = mongo_store.logs

@app.route('/')
def webprint():
    return render_template('hompage.html')


@app.route('/categorypage/<categoryname>')
def categorypage(categoryname):
    categories = metadata.find({'categories': {"$elemMatch": {"$elemMatch": {"$eq": categoryname} } }}, {'imUrl': 1, 'asin': 1, '_id': 0 })

    categories = [i for i in categories]
    # to set limit to how many you want to add
    limit = 10
    # return render_template('categorypage2.html')
    return render_template('categorypage2.html', categories=categories[:limit], name=categoryname)

@app.route('/book/<asin>')
def book(asin):

    ### THIS FUNCTION WILL USE BOTH MYSQL AND MONGO TO FILL UP THE BOOK PAGE 
    reviews = metadata.find({'asin': asin})

    return render_template('review.html', reviews=reviews)

@app.route('/reviews', methods=['GET','POST'])
def reviews():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        name = userDetails['name']
        asin = userDetails['asin']
        review = userDetails['review']
        summary = userDetails['summary']
        overall = request.form.get['overall']
        reviewTime= request.form.get['reviewTime']
        unixReviewTime= userDetails ['unixReviewTime']
        cur = mysql.connection.cursor()
        # Create a database called test and create necessary tables
        cur.execute("INSERT INTO test(reviewerName,asin,reviewText,summary,overall,reviewTime,unixReviewTime) VALUES(%s,%s,%s,%s,%s,%s,%s)"
                            ,(name,asin,review,summary,overall,reviewTime,unixReviewTime))
        # Save changes into the database
        mysql.connection.commit()
        cur.close()
        return 'update successful'
    return render_template('')


if __name__ == "__main__":
    app.run(debug=True)
