import './Stock.css';
import React, { useState, useEffect } from 'react';
import StockTable from './StockTable.js';
import UserList from './UserList.js';
import { socket } from '../App.js';

const Stock = (props) => {
    const [stocks, setStocks] = useState({});
    const [likedStocks, setLikedStocks] = useState([]);
    const [userList, setUserList] = useState([]);
    
    // Request the list of all stocks from the server using the '/stocks'
    // path. The server would retrieve the records from the Stocks table in the
    // database via SQLAlchemy model and return the results in JSON format.
    useEffect(() => {
        fetch('/stocks')
        .then(res => res.json())
        .then(data => {
            console.log(data)
            setStocks(data.stocks_data);
            data.display_list.map((user) => console.log(user));
            setUserList(data.display_list)
        });

        fetch("/get_liked_stocks", {
            method: "POST",
            headers: {
                "Content-Type": "application/json; charset=utf-8",
            },
            body: JSON.stringify({email: props.email})
        })
        .then(res => res.json())
        .then(data => {
            setLikedStocks(data.myLikedStocks);
        });
        
        socket.on('login' , (data) => { // [array of users]
            if(data !== undefined){
                console.log(data);
                setUserList(data);
                // data.map((user) => console.log(user));
            }
        });
        socket.on('logout' , (data) => { // [array of users]
            if(data !== undefined){
                console.log(data);
                setUserList(data);
                // data.map((user) => console.log(user));
            }
        });
        
    }, []);

    if (Object.keys(stocks).length) {
        const megaStocks = stocks.allStocks.filter((stock) => stock.Category === 'Mega');
        const techStocks = stocks.allStocks.filter((stock) => stock.Category === 'Tech');
        const finStocks = stocks.allStocks.filter((stock) => stock.Category === 'Finance');
        const utilStocks = stocks.allStocks.filter((stock) => stock.Category === 'Utilities');
        const energyStocks = stocks.allStocks.filter((stock) => stock.Category === 'Energy');

        return (
            <div>
                <div id="page_body">
                    <h3>Click on a row to go to that stock's discussion page</h3>
                </div>
                    
                <div className="container">
                    <div className="stock-list">
                        <h2 className="sector-title">Energy</h2>
                        <StockTable 
                            stocks={energyStocks}
                            email={props.email}
                            likedStocks={likedStocks}
                            setLikedStocks={setLikedStocks} />
                        <h2 className="sector-title">Finance</h2>
                        <StockTable
                            stocks={finStocks}
                            email={props.email}
                            likedStocks={likedStocks}
                            setLikedStocks={setLikedStocks} />
                        <h2 className="sector-title">Mega</h2>
                        <StockTable
                            stocks={megaStocks}
                            email={props.email}
                            likedStocks={likedStocks}
                            setLikedStocks={setLikedStocks} />
                        <h2 className="sector-title">Tech</h2>
                        <StockTable
                            stocks={techStocks}
                            email={props.email}
                            likedStocks={likedStocks}
                            setLikedStocks={setLikedStocks} />
                        <h2 className="sector-title">Utilities</h2>
                        <StockTable
                            stocks={utilStocks}
                            email={props.email}
                            likedStocks={likedStocks}
                            setLikedStocks={setLikedStocks} />
                    </div>
                    
                    <div className="user-list">
                        <h2 className ="investors-title">Investors</h2>
                        
                        <table id="user_table">
                            <thead>
                                {userList.map((user, index) => {
                                    return (
                                        <tr><td>{user}</td></tr>
                                    );
                                })}
                            </thead>
                        </table>
                    </div>
                </div>
            </div>
        );
    }

    return (
        <div id="page_body">
            ...Loading
        </div>
    )
}

export default Stock;