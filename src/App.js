import logo from './logo.svg';
import './App.css';
import React, { useState } from "react";
import { BrowserRouter as Router, Route, Switch, Link } from "react-router-dom";
import Login from './components/Login.js';
import Logout from './components/Logout.js';

import Home from './components/Home.js';
import Stock from './components/Stock.js'
import StockPage from './components/StockPage.js'

function App() {
  
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  
  function authenticated(){
    setIsLoggedIn(!isLoggedIn);
  }
  
  if (isLoggedIn){
    return (
      <div className="App">
        <Router>
          <header className="App-header">
          Stock XChange!
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
        <header className="App-header">
          Stock XChange
        </header>
<<<<<<< HEAD
        <Login authenticated={authenticated}/>
      </div>
    );
=======
        <div>
          <nav className="navbar">
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
            <Route 
              path="/stock_page/:symbol" 
              render={(props) => <StockPage id={props.match.params.symbol} />}>
            </Route>
          </Switch>
        </div>
      </Router>
          
    </div>
  );
>>>>>>> 6cb4ec2f1a4805560c5409689de7fc8deb415d1f
}

export default App;
