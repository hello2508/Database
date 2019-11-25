import React from 'react';
import './categories.css';
import { NavLink } from 'react-router-dom';

class Cat extends React.Component {
  render (){
    return (
      <div classNameName="Cat">
      <header name="header">
            <nav>
                <div className="row nav-bar">
                    <p className="company-name">
                    Great Reads 
                    </p>
                    <NavLink to="/categories"><a className="active" href="#"><i className="fa fa-fw fa-user"></i> Categories</a></NavLink>
                    <NavLink to="/addreview"><a className="nactive" href="#"><i className="fa fa-fw fa-user"></i> Review</a></NavLink> 
                    <NavLink to="/"><a className="nactive" href="#"><i className="fa fa-fw fa-user"></i> Home</a></NavLink>
                </div>
                </nav>
            </header>
            <section className="section-space">
                <div>
                    <div className="background-image">
                        <p>&nbsp;</p>
                    </div>
                </div>
                <div className="row">
                    <div className="category-portion">
                        <h1 className="category-heading">Category</h1>
                        <div className="row category-book-row">
                            <a href=""><img src="img/1713426._SX98_.png" className="book-img"/></a>
                            <a href=""><img src="img/1713426._SX98_.png" className="book-img"/></a><a href=""><img src="img/1713426._SX98_.png" className="book-img"/></a><a href=""><img src="img/1713426._SX98_.png" className="book-img"/></a><a href=""><img src="img/1713426._SX98_.png" className="book-img"/></a><a href=""><img src="img/1713426._SX98_.png" className="book-img"/></a><a href=""><img src="img/1713426._SX98_.png" className="book-img"/></a>
                            
                            <div className="hover-over-description">
                                <h1 className="bookname">Predictably Irrational</h1>
                                <h2 className="author">by Dan &amp; Ariely</h2>
                                <p className="book-des">Predictably Irrational: The Hidden Forces That Shape Our Decisions is a 2008 book by Dan Ariely, in which he challenges readers' assumptions about making decisions based on rational thought.</p>
                            </div>
                        </div>
                    </div>
                    <div className="side-panel">
                        <div className="enjoyed-books-section">
                            <h2 className="reader-enjoy-heading">Readers also enjoyed:</h2>
                            <img src="img/929._SX98_.png" className="enjoyed-books"/>
                            <img src="img/2776527._SX98_.png" className="enjoyed-books"/>
                            <img src="img/2776527._SX98_.png" className="enjoyed-books"/>
                            <h3 className="similar-books">See similar books...</h3>
                        </div>
                        <div className="write-review">
                            <h1 className="review-heading">Want to write a review?</h1>
                            <p>click here!</p>
                        </div>
                    </div>
                </div>
            </section>
      </div>
    );
    }
}


export default Cat;
