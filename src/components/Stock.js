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
            <div>
                <div id="page_body">
                    <h2>Click on a row to go to that stock's discussion page.</h2>
                        All filters result in data in descending order. <br/>
                </div>
                    
                <div className="container">
                    <div className="stock-list">
                        <h2 className="sector-title">Energy</h2>
                        <StockTable stocks={energyStocks} />
                        <h2 className="sector-title">Finance</h2>
                        <StockTable stocks={finStocks} />
                        <h2 className="sector-title">Mega</h2>
                        <StockTable stocks={megaStocks} />
                        <h2 className="sector-title">Tech</h2>
                        <StockTable stocks={techStocks} />
                        <h2 className="sector-title">Utilities</h2>
                        <StockTable stocks={utilStocks} />
                    </div>
                    
                    <div className="user-list">
                        <h2 className ="investors-title">Investors</h2>
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