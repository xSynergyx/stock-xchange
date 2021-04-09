import logo from './logo.svg';
import './App.css';
import React, { useState } from "react";
import { BrowserRouter as Router, Route, Switch, Link } from "react-router-dom";
import Login from './components/Login.js';
import Logout from './components/Logout.js';

import Home from './components/Home.js';
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
          <header>
          Stock XChange
          </header>
          <div>
            <nav>
              <ul>
                <li>
                  <Link to="/home">Home</Link>
                </li>
                <li>
                  <Link to="/stock">Stock Page</Link>
                </li>
              </ul>
            </nav>
            
            <Switch>
              <Route path="/stock">
                <Stock />
              </Route>
              <Route path="/home">
                <Home />
              </Route>
            </Switch>
          </div>
        </Router>
        <Logout authenticated={authenticated}/>
            
      </div>
    );
  }
  
  return (
      <div className="App">
        <Login authenticated={authenticated}/>
      </div>
    );
}

export default App;
