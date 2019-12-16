

#Import Kindle Reviews into EC2 instance



# ====MYSQL====
# Creating table for kindle_reviews
CREATE TABLE kindle_reviews(
id int UNIQUE AUTO_INCREMENT,
asin varchar(10),  
helpful varchar(15), 
overall int(1),
reviewText text(32767), 
reviewTime varchar(11), 
reviewerID varchar(25), 
reviewerName varchar(80),
summary varchar(750), 
unixReviewTime int(10)
);