import React, { Component } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import axios from 'axios';
import Home from './components/Homepage';
import Review from './components/addReview';
import Cat from './components/categories';

 
class App extends Component {
  render() {
    return (      
       <BrowserRouter>
        <div>
            <Switch>
             <Route path="/" component={Home} exact/>
             <Route path="/addreview" component={Review}/>
             <Route path="/categories" component={Cat}/>
           </Switch>
        </div> 
      </BrowserRouter>
    );
  }
}
 
export default App;
