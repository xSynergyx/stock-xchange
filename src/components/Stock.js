import './Stock.css';
import React, { useState, useEffect } from 'react';
import StockTable from './StockTable.js'

function Stock() {
    const [stocks, setStocks] = useState({});
    
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
            <div id="page_body">
                <h2>Click on a row to go to that stock's discussion page.</h2>
                <StockTable stocks={stocks.allStocks} />
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