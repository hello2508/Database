import React from 'react';
import logo from './logo.svg';
import './Homepage.css';

class Home extends React.Component {
  render (){
    return (
      <div classNameName="App">
      <header name="header">
      <nav>
          <div className="row nav-bar">
              <p classNameName="company-name">
              Great Reads
              </p>

              <a className="nactive" href="#"><i className="fa fa-fw fa-user"></i> Login</a>
              <a className="nactive" href="#"><i className="fa fa-fw fa-search"></i> Search</a>
              <a className="active" href="hompage.html"><i className="fa fa-fw fa-home"></i> Home</a>
          </div>


          <div className="row" name="space">
              <div className="col span-3-of-4 column-left">
                  <div className="background-image">
                      <p>&nbsp;</p>
                  </div>

                  <div className="searchbar">
                      <h2 className="search-font">
                      Search and browse books
                      </h2>
                      <div className="wrap">
                         <div className="search">
                            <input type="text" className="searchTerm" placeholder="What are you looking for?">
                            <button type="submit" className="searchButton">
                              <i className="fa fa-search"></i>
                           </button>
                         </div>
                      </div>
                      <h1 className="top-cat">Top Categories:</h1>
                      <div className="">
                          <div className="col span-1-of-4">
                              <p className="genre-links"><a href="categorypage.html">Arts &#38; Photography</a></p>
                              <p className="genre-links"><a href="">Biographies &#38; Memoirs</a></p>
                              <p className="genre-links"><a href="">Books</a></p>
                              <p className="genre-links"><a href="">Business &#38; Money</a></p>
                              <p className="genre-links"><a href="">Children's Books</a></p>
                              <p className="genre-links"><a href="">Children's eBooks</a></p>
                              <p className="genre-links"><a href="">Christian Books &#38; Bibles</a></p>
                              <p className="genre-links"><a href="">Computers &#38; Technology</a></p>
                          </div>
                          <div className="col span-1-of-4">
                              <p className="genre-links"><a href="">Cookbooks, Food &#38; Wine</a></p>
                              <p className="genre-links"><a href="">Crafts, Hobbies &#38; Home</a></p>
                              <p className="genre-links"><a href="">Engineering</a></p>
                              <p className="genre-links"><a href="">Europe</a></p>
                              <p className="genre-links"><a href="">Foreign Languages</a></p>
                              <p className="genre-links"><a href="">Health, Fitness &#38; Dieting</a></p>
                              <p className="genre-links"><a href="">History</a></p>
                              <p className="genre-links"><a href="">Humor &#38; Entertainment</a></p>
                          </div>
                          <div className="col span-1-of-4">
                              <p className="genre-links"><a href="">Kindle eBooks</a></p>
                              <p className="genre-links"><a href="">Kindle Store</a></p>
                              <p className="genre-links"><a href="">Law</a></p>
                              <p className="genre-links"><a href="">Literature &#38; Fiction</a></p>
                              <p className="genre-links"><a href="">Medical Books</a></p>
                              <p className="genre-links"><a href="">Medical eBooks</a></p>
                              <p className="genre-links"><a href="">Politics &#38; Social Sciences</a></p>
                              <p className="genre-links"><a href="">Professional &#38; Technical</a></p>
                          </div>
                          <div className="col span-1-of-4">
                              <p className="genre-links"><a href="">Reference</a></p>
                              <p className="genre-links"><a href="">Religion &#38; Spirituality</a></p>
                              <p className="genre-links"><a href="">Science &#38; Math</a></p>
                              <p className="genre-links"><a href="">Sports &#38; Outdoors</a></p>
                              <p className="genre-links"><a href="">Travel</a></p>
                              <p className="genre-links"><a href="">United States</a></p>
                              <p className="genre-links more-genres"><a href="">More Genres...</a></p>
                          </div>
                      </div>
                  </div>
              </div>
              <div className="col span-1-of-4">
                  <div name="side-col">
                  <h1 className="top-picks">Top Picks</h1>
                      <div className="top-picks-col">
                          <div className="col span-1-of-3 imgcol1">
                              <a href="">
                                  <img src="UI/1713426._SX98_.png" className="book-inbetween">
                              </a>
                              <a href="">
                                  <img src="UI/43641._SX98_.png" className="book-inbetween">
                              </a>
                              <a href="">
                                  <img src="UI/1713426._SX98_.png" className="book-inbetween">
                              </a>
                          </div>
                      <div className="col span-1-of-3 imgcol1">
                          <a href="">
                              <img src="UI/929._SX98_.png" className="book-inbetween">
                          </a>
                          <a href="">
                              <img src="UI/39832183._SX98_.png" className="book-inbetween">
                          </a>
                          <a href="">
                              <img src="UI/1713426._SX98_.png" className="book-inbetween">
                          </a>
                      </div>
                      <div className="col span-1-of-3 imgcol1">
                          <a href="">
                              <img src="UI/43641._SX98_.png" className="book-inbetween">
                          </a>
                          <a href="">
                              <img src="UI/929._SX98_.png" className="book-inbetween">
                          </a>
                          <a href="">
                              <img src="UI/1713426._SX98_.png" className="book-inbetween">
                          </a>
                      </div>
                      <div className="button">
                          <a href="" className="more-button"><span className="more-toppicks">More >>> </span></a>
                      </div>
                  </div>
                  </div>
              </div>

          </div>
      </nav>
      </header>
      </div>
    );
  }

export default Home;
