import React, { useState } from 'react';
import './StockTable.css';
import { useHistory } from "react-router-dom";
import { AiFillLike, AiOutlineLike, AiFillDislike, AiOutlineDislike } from 'react-icons/ai';

const CryptoTable = (props) => {
    const headers = ['Symbol', 'Price'];
    const history = useHistory();
    const [tableData, setTableData] = useState(props.stocks);

    // Redirect to the selected stock's page
    // when the user clicks on a row in the list
    // Check App.js for the Route this triggers

    const filterData = (filter) => {
        switch (filter) {
            case 'Price':
                setTableData((oldTable) => {
                    let newTable = [...oldTable];
                    return newTable.sort((a, b) => (a.Price > b.Price) ? -1 : 1);
                });
            break;
            default:
                setTableData((oldTable) => {
                    return props.stocks;
                });
        }
    }

    return (
        <div id="page_body">
            <div className="filters">
                <span class="tooltiptext">All filters result in descending order</span>
                <input
                    onClick={() => filterData('Price')}
                    type="radio" 
                    name="filter" />Price
            </div>
            <table id="stocks_table" data-testid="stocks_table">
                <thead>
                    <tr className="header-row">
                        <td><p>Symbol</p></td>
                        <td><p>Price</p></td>
                    </tr>
                </thead>
                <tbody>
                    {tableData.map((stock) => {
                        return (
                            <tr id={stock.Symbol} className="border_bottom">
                                {headers.map((header) => (
                                    <td>{stock[header]}</td>
                                ))}
                                <Like
                                    symbol={stock.Symbol}
                                    email={props.email}
                                    likedStocks={props.likedStocks}
                                    setLikedStocks={props.setLikedStocks} />
                            </tr>
                        );
                    })}
                </tbody>
            </table>
        </div>
    )
}

export const Like = (props) => {
    const [isClicked, setClicked] = useState(false);

    const onLike = () => {
        // Call server to figure out
        // if it's a like / dislike
        fetch("/like_stock", {
            method: "POST",
            headers: {
                "Content-Type": "application/json; charset=utf-8",
            },
            body: JSON.stringify({stock_symbol: props.symbol, email: props.email})
        });

        if (isClicked || props.likedStocks.filter((stock) => stock.Symbol === props.symbol).length > 0) {
            // Update liked stocks list to re-render component
            props.setLikedStocks((oldStocks) => {
                const newStocks = [...oldStocks];
                return newStocks.filter((stock) => stock.Symbol != props.symbol);
            })
            setClicked(false);
        }

        else {
            setClicked(true);
        }
    }

    // Check if button has been clicked or stock is in the user's liked stocks, in which case
    // the button should indicate that it's pressed
    if (isClicked || props.likedStocks.filter((stock) => stock.Symbol === props.symbol).length > 0) {
        return (
            <td id="fill_like" onClick={onLike}><AiFillLike size='1.5em' /></td>
        );
    }

    else {
        return (
            <td id="outline_like" onClick={onLike}><AiOutlineLike size='1.5em' /></td>
        );
    }
}

export default CryptoTable;