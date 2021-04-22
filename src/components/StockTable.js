import React, { useState } from 'react';
import './StockTable.css';
import { useHistory } from "react-router-dom";

const StockTable = (props) => {
    const headers = ['Symbol', 'Company', 'High', 'Low', 'Price'];
    const history = useHistory();
    const [tableData, setTableData] = useState(props.stocks);

    // Redirect to the selected stock's page
    // when the user clicks on a row in the list
    // Check App.js for the Route this triggers
    const onRowClick = (stock_symbol) => {
        history.push('/stock_page/' + stock_symbol);
    }

    const filterData = (filter) => {
        switch (filter) {
            case 'Price':
                setTableData((oldTable) => {
                    let newTable = [...oldTable];
                    return newTable.sort((a, b) => (a.Price > b.Price) ? -1 : 1);
                });
            break;
            case 'High':
                setTableData((oldTable) => {
                    let newTable = [...oldTable];
                    return newTable.sort((a, b) => (a.High > b.High) ? -1 : 1);
                });
            break;
            case 'Low':
                setTableData((oldTable) => {
                    let newTable = [...oldTable];
                    return newTable.sort((a, b) => (a.Low > b.Low) ? -1 : 1);
                });
            break;
            case 'Company':
                setTableData((oldTable) => {
                    let newTable = [...oldTable];
                    return newTable.sort((a, b) => (a.Company < b.Company) ? -1 : 1);
                });
            break;
            default:
                setTableData((oldTable) => {
                    return props.stocks;
                });
        }
    }

    return (
        <div>
            <div>
                <input
                    onClick={() => filterData('Price')}
                    type="radio" 
                    name="filter" />Price
                <input
                    onClick={() => filterData('High')}
                    type="radio"
                    name="filter"/>High
                <input
                    onClick={() => filterData('Low')}
                    type="radio"
                    name="filter"/>Low
                <input
                    onClick={() => filterData('Company')}
                    type="radio"
                    name="filter"/>Company Name
            </div>
            <table id="stocks_table" data-testid="stocks_table">
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
                    {tableData.map((stock) => {
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