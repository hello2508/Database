import React from 'react';
import './addreview.css';
import { NavLink } from 'react-router-dom';

class Review extends React.Component {
  render (){
    return (
      <div classNameName="Review">
      <header name="header">
            <nav>
                <div className="row nav-bar">
                    <p className="company-name">
                    Great Reads 
                    </p>
                    <NavLink to="/categories"><a className="nactive" href="#"><i className="fa fa-fw fa-user"></i> Categories</a></NavLink>
                    <NavLink to="/addreview"><a className="active" href="#"><i className="fa fa-fw fa-user"></i> Review</a></NavLink> 
                    <NavLink to="/"><a className="nactive" href="#"><i className="fa fa-fw fa-user"></i> Home</a></NavLink>
                </div>
                <div className="pop-up">
                        <img src="UI/39832183._SX98_.png" className="review-img" align="left"/>
                        <div className="review-deets">
                        <h1 className="review-heading">Write a Review!</h1>
                        <p className="book-details">Name of Book:</p>
                        <p className="book-details">Author:</p>
                        <p className="book-details">Publisher:</p>
                        </div>
                    <div className="form-fields">
                        <div className="col span-1-of-3 fields">
                            <h1 className="field-names">Your Name:</h1>
                            <h1 className="field-names">User ID:</h1>
                            <h1 className="field-names">Review Description:</h1>
                            <h1 className="field-names">Ratings:</h1>
                        </div>
                        <div className="col span-2-of-3">
                            <textarea rows="1" cols="100" name="comment" form="usrform" className="top-field small-input-field">Enter text here...
                            </textarea>
                            <textarea rows="1" cols="100" name="comment" form="usrform" className="top-field small-input-field">Enter text here...
                            </textarea>
                            <textarea rows="1" cols="100" name="comment" form="usrform" className="top-field small-input-field">Enter text here...
                            </textarea>
                            <textarea rows="1" cols="100" name="comment" form="usrform" className="top-field small-input-field">Enter text here...
                            </textarea>
                        </div>
                    </div>
                    <div className="submit-button">
                            <a href="" className="submitclickbutton"><span className="more-toppicks">Submit</span></a>
                    </div>
                </div>
                
                
            </nav>
            </header>
      </div>
    );
    }
}


export default Review;
