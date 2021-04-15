import './Stock.css';
import React, { useState, useEffect } from 'react';
import { useHistory } from "react-router-dom";
import StockTable from './StockTable.js'

function Stock() {
    const [stocks, setStocks] = useState({});
    const headers = ['Symbol', 'Name', 'Price (Intraday)', 'Change', 'Market Cap']
    
    // Request the list of all stocks from the server using the '/stocks'
    // path. The server would retrieve the records from the Stocks table in the
    // database via SQLAlchemy model and return the results in JSON format.
    useEffect(() => {
        fetch('/stocks')
        .then(res => res.json())
        .then(data => {
            setStocks(data);
        });
    }, []);

    if (Object.keys(stocks).length) {
        return (
            <div>
                <h2>Click on a row to go to that stock's discussion page.</h2>
                <StockTable stocks={stocks.allStocks} />
            </div>
        );
    }
    
    return (
        <div>
            ...Loading
        </div>
    )
}

export default Stock;