import logo from './logo.svg';
import './App.css';
import React from "react";
import { BrowserRouter as Router, Route, Switch, Link } from "react-router-dom";

import Home from './components/Home.js';
import Stock from './components/Stock.js'
import StockPage from './components/StockPage.js'

function App() {
  return (
    <div className="App">
      <Router>
        <header>
        Stock XChange
        </header>
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
              path="/stock_page/:id"
              render={(props) => <StockPage id={props.match.params.id}/>}>
            </Route>
          </Switch>
        </div>
      </Router>
          
    </div>
  );
}

export default App;
