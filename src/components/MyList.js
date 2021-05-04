import './MyList.css';
import React, { useState, useEffect } from 'react';
import StockTable from './StockTable.js';

const MyList = (props) => {
    const [likedStocks, setLikedStocks] = useState({});

    useEffect(() => {
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
    }, []);
    
    if (Object.keys(likedStocks).length) {
        return (
            <div className="my-list-container">
                <h2 className="sector-title">Watchlist</h2>
                <StockTable 
                    stocks={likedStocks}
                    email={props.email}
                    likedStocks={likedStocks}
                    setLikedStocks={setLikedStocks} />
            </div>
        );
    }
    else {
        return (
            <div>
                Loading...
            </div>
        )
    }
}

export default MyList;