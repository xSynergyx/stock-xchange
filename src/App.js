import logo from './logo.svg';
import './App.css';
import React, { useState } from "react";
import { BrowserRouter as Router, Route, Switch, Link } from "react-router-dom";
import Login from './components/Login.js';
import Logout from './components/Logout.js';

import Profile from './components/Profile.js';
import MyList from './components/MyList.js';
import Stock from './components/Stock.js';
import SearchBar from './components/SearchBar.js';



function App() {
  
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [username, setUsername] = useState("Profile");
  
  function authenticated(){
    setIsLoggedIn(!isLoggedIn);
  }
  
  function updateUsername(newUsername){
    setUsername(newUsername);
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
                  <Link to="/profile">{ username }</Link>
                </li>
                <li className="navbar">
                  <Link to="/mylist">My List</Link>
                </li>
                <li className="navbar">
                  <Link to="/stock">Stock Page</Link>
                </li>
                <li className ="navbar-right">
                  <Logout authenticated={authenticated}/>
                </li>
                <li className="navbar-right">
                  <SearchBar />
                </li>
              </ul>
            </nav>
            
            <Switch>
              <Route path="/mylist">
                <MyList />
              </Route>
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
        <Login authenticated={authenticated} updateUsername={updateUsername}/>
      </div>
    );
}

export default App;
