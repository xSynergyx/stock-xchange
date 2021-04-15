import logo from './logo.svg';
import './App.css';
import React, { useState } from "react";
import { BrowserRouter as Router, Route, Switch, Link } from "react-router-dom";
import Login from './components/Login.js';
import Logout from './components/Logout.js';

import Profile from './components/Profile.js';
import Stock from './components/Stock.js';



function App() {
  
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  
  function authenticated(){
    setIsLoggedIn(!isLoggedIn);
  }
  
  if (isLoggedIn){
    return (
      <div className="App">
        <Router>
          <div>
            <nav>
              <ul>
                <li className="navbar-header">
                  <Link to="/">Stock XChange</Link>
                </li>
                <li className="navbar">
                  <Link to="/profile">Profile</Link>
                </li>
                <li className="navbar">
                  <Link to="/stock">Stock Page</Link>
                </li>
                <li className ="navbar-right">
                  <Logout authenticated={authenticated}/>
                </li>
              </ul>
            </nav>
            
            <Switch>
              <Route path="/stock">
                <Stock />
              </Route>
              <Route path="/profile">
                <Profile />
              </Route>
              <Route path="/">
                <p>Stock List Component goes in here</p>
              </Route>
            </Switch>
          </div>
        </Router>
            
      </div>
    );
  }
  
  return (
      <div className="App">
        <ul>
          <li className="navbar-home">
            Stock XChange
          </li>
        </ul>
        <Login authenticated={authenticated}/>
      </div>
    );
}

export default App;
