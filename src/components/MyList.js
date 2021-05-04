import './MyList.css';
import React, { useState, useEffect } from 'react';
import StockTable from './StockTable.js';

const MyList = (props) => {
    const [likedStocks, setLikedStocks] = useState({});
    const [loadedLiked, setLoadedLiked] = useState(false);

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
            setLoadedLiked(true);
        });
    }, []);
    
    if (Object.keys(likedStocks).length) {
        return (
            <div id="page_body">
                <StockTable 
                    stocks={likedStocks}
                    email={props.email}
                    likedStocks={likedStocks}
                    setLikedStocks={setLikedStocks} />
            </div>
        );
    }
    else if (loadedLiked && Object.keys(likedStocks).length === 0) {
        return (
            <div id="message">
                You haven't liked any stocks
            </div>
        );
    }
    else {
        return (
            <div id="message">
                Loading...
            </div>
        )
    }
}

export default MyList;