import './App.css';
import React, { useState } from "react";
import { BrowserRouter as Router, Route, Switch, Link } from "react-router-dom";
import Login from './components/Login.js';
import Logout from './components/Logout.js';

import Profile from './components/Profile.js';
import MyList from './components/MyList.js';
import Stock from './components/Stock.js';
import SearchBar from './components/SearchBar.js';
import StockPage from './components/StockPage.js';
import logo from './images/logo.png';
import invest from './images/invest.jpg';

import io from 'socket.io-client';
const socket = io(); // Connects to socket connection

function App() {
  
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [username, setUsername] = useState("Profile");
  const [email, setEmail] = useState("");

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
                  <Link to="/"><img src={ logo } width="200px" height="35px"/></Link>
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
                <MyList email={email} />
              </Route>
              <Route path="/stock">
                <Stock email={email} />
              </Route>
              <Route path="/profile">
                <Profile username={username} email={email} />
              </Route>
              <Route 
                path="/stock_page/:symbol"
                render={(props) => (
                  <StockPage 
                    symbol={props.match.params.symbol}
                    username={username}
                    email={email} />
                )}
              >
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
          <img src={ logo } width="200px" height="35px"/>
        </li>
      </ul>
      
      
      <div className="image-container">
        <p className="slide-right">Whether you are experienced or a complete beginner, 
                                    StockXChange allows investors to easily recommend stocks,
                                    help fellow investors and receive guidance. Together we profit.</p>
        <div className="fade-in-image">
          <img src={ invest } width="100%" height="100%"/>
        </div>
      </div>
      
      
      <Login authenticated={authenticated} updateUsername={updateUsername} setEmail={setEmail} />
    </div>
  );
}

export default App;
export { socket };