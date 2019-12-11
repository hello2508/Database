from flask import Flask, render_template, jsonify, url_for, request, redirect
# from flask_pymongo import PyMongo
from pymongo import MongoClient
from bson.json_util import dumps
import mysql.connector

app = Flask(__name__)  #creates an app

### Kenneth's EC2 instance
mongo_store = MongoClient("mongodb://18.141.0.98/")
metadata = mongo_store.goodread.metadata

### My own local
# mongo_store = MongoClient("mongodb://localhost:27017")
# metadata = mongo_store.nezukodb.metadata
# logs = mongo_store.nezukodb.logs
# logs = mongo_store.logs

#### MYSQL
# Configure db
db = mysql.connector.connect(
    host = '18.141.90.224',
    user = 'root',
    password = '',
    database = 'dbds',
    buffered = True
    )


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
    limit = 50
    # return render_template('categorypage2.html')
    return render_template('categorypage2.html', categories=categories[:limit], name=categoryname)

@app.route('/book/<asin>', methods=['GET','POST'])
def book(asin):

    ### THIS FUNCTION WILL USE BOTH MYSQL AND MONGO TO FILL UP THE BOOK PAGE
    reviews = metadata.find({'asin': asin})

    cur = db.cursor()
    # Add new review and update database
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form

        overall = userDetails['overall']
        review = userDetails['review']
        reviewTime= userDetails['reviewTime']
        ID = userDetails['ID']
        name = userDetails['name']
        summary = userDetails['summary']
        unixReviewTime= userDetails ['unixReviewTime']
        cur.execute("INSERT INTO test(asin,helpful,overall,reviewText,reviewTime,reviewerID,reviewerName,summary,unixReviewTime) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                            ,(asin,0,overall,review,reviewTime,ID,name,summary,unixReviewTime))
        # Save changes into the database
        db.commit()
        cur.close()

    # Getting reviews for specific asin
    # cur.execute("SELECT asin, reviewerName, reviewText FROM kindle_reviews WHERE asin='B000F83SZQ' LIMIT 10") --- WORKS LIKE A CHARM
    reviews_query = "SELECT asin, reviewerName, reviewText FROM kindle_reviews WHERE asin= %s LIMIT 10"
    cur.execute(reviews_query, (asin,))
    bookasin = cur.fetchall()

    searchasin =  "SELECT asin FROM kindle_reviews WHERE asin= %s LIMIT 1"   
    cur.execute(asinforbook, (asin,))
    asinforbook = cur.fetchall()
    # for bookreviews in bookasin:
    #     print(bookreviews)
    return render_template('review.html', reviews=reviews, bookasin=bookasin, asinforbook=asinforbook)

    # return render_template('review.html', reviews=reviews)

@app.route('/addbook')
def adminaddbook():
    return render_template('addBook.html')


if __name__ == "__main__":
    app.run(debug=True)
