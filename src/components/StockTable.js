import React, { useState } from 'react';
import './StockTable.css';
import { useHistory } from "react-router-dom";
import { AiFillLike, AiOutlineLike, AiFillDislike, AiOutlineDislike } from 'react-icons/ai';

const StockTable = (props) => {
    const headers = ['Symbol', 'Company', 'High', 'Low', 'Price'];
    const history = useHistory();
    const [tableData, setTableData] = useState(props.stocks);

    // Redirect to the selected stock's page
    // when the user clicks on a row in the list
    // Check App.js for the Route this triggers
    const onRowClick = (stock_symbol) => {
        const isLiked =
            props.likedStocks.filter((stock) => stock.Symbol === stock_symbol).length > 0 ? true: false;

        history.push({
            pathname: '/stock_page/' + stock_symbol,
            state: {isLiked: isLiked}
        });
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
        <div id="page_body">
            <div className="filters">
                <span class="tooltiptext">All filters result in descending order</span>
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
                    <tr className="header-row">
                        <td><p>Symbol</p></td>
                        <td><p>Company</p></td>
                        <td><p>High</p></td>
                        <td><p>Low</p></td>
                        <td><p>Price</p></td>
                    </tr>
                </thead>
                <tbody>
                    {tableData.map((stock) => {
                        return (
                            <tr id={stock.Symbol} className="border_bottom">
                                {headers.map((header) => (
                                    <td onClick={() => onRowClick(stock.Symbol)}>{stock[header]}</td>
                                ))}
                                <Like
                                    symbol={stock.Symbol}
                                    email={props.email}
                                    likedStocks={props.likedStocks}
                                    setLikedStocks={props.setLikedStocks} 
                                    totalLikes={stock.Likes} />
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
            <td id="fill_like" onClick={onLike}><AiFillLike size='1.5em' />{props.totalLikes + 1}</td>
        );
    }

    else {
        return (
            <td id="outline_like" onClick={onLike}><AiOutlineLike size='1.5em'/>{props.totalLikes}</td>
        );
    }
}

export default StockTable;