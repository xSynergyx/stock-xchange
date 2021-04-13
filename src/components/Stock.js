import './Stock.css';
import React, { useState, useEffect } from 'react';
import { useHistory } from "react-router-dom";

function Stock() {
    const [stocks, setStocks] = useState([]);
    const headers = ['Symbol', 'Name', 'Price (Intraday)', 'Change', 'Market Cap']
    const history = useHistory();
    
    // Request the list of all stocks from the server using the '/stocks'
    // path. The server would retrieve the records from the Stocks table in the
    // database via SQLAlchemy model and return the results in JSON format.
    useEffect(() => {
        fetch('/stocks')
        .then(res => res.json())
        .then(data => {
            setStocks(data.allStocks);
        });
    }, []);

    // Redirect to the selected stock's page
    // when the user clicks on a row in the list
    // Check App.js for the Route this triggers
    const onRowClick = (stock_symbol) => {
        history.push('/stock_page/' + stock_symbol);
    }

    return (
        <div>
            <h2>Click on a row to go to that stock's discussion page.</h2>
            <table id="stocks_table">
                <thead>
                    <tr>
                        <td>Symbol</td>
                        <td>Name</td>
                        <td>Price (Intraday)</td>
                        <td>Change</td>
                        <td>Market Cap</td>
                    </tr>
                </thead>
                <tbody>
                    {stocks.map((stock) => {
                        return (
                            <tr id={stock.Symbol} onClick={() => onRowClick(stock.Symbol)}>
                                {headers.map((header) => (
                                    <td>{stock[header]}</td>
                                ))}
                            </tr>
                        );
                    })}
                </tbody>
            </table>
        </div>
    );
}

export default Stock;