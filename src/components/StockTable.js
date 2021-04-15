import React from 'react';
import { useHistory } from "react-router-dom";

const StockTable = (props) => {
    const headers = ['Symbol', 'Company', 'High', 'Low', 'Price']
    const history = useHistory();

    // Redirect to the selected stock's page
    // when the user clicks on a row in the list
    // Check App.js for the Route this triggers
    const onRowClick = (stock_symbol) => {
        history.push('/stock_page/' + stock_symbol);
    }

    return (
        <div>
            <table id="stocks_table">
                <thead>
                    <tr>
                        <td>Symbol</td>
                        <td>Company</td>
                        <td>High</td>
                        <td>Low</td>
                        <td>Price</td>
                    </tr>
                </thead>
                <tbody>
                    {props.stocks.map((stock) => {
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
    )
}

export default StockTable;