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
        const megaStocks = stocks.allStocks.filter((stock) => stock.Category === 'Mega');
        const techStocks = stocks.allStocks.filter((stock) => stock.Category === 'Tech');
        const finStocks = stocks.allStocks.filter((stock) => stock.Category === 'Finance');
        const utilStocks = stocks.allStocks.filter((stock) => stock.Category === 'Utilities');
        const energyStocks = stocks.allStocks.filter((stock) => stock.Category === 'Energy');

        return (
            <div id="page_body">
                <h2>Click on a row to go to that stock's discussion page.</h2>
                All filters result in data in descending order. <br/>
                Energy
                <StockTable stocks={energyStocks} />
                Finance
                <StockTable stocks={finStocks} />
                Mega
                <StockTable stocks={megaStocks} />
                Tech
                <StockTable stocks={techStocks} />
                Utilities
                <StockTable stocks={utilStocks} />
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