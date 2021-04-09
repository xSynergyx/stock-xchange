import React , { useState, useEffect } from 'react';

const StockPage = (props) => {
    const [pageData, setPageData] = useState({})
    const [stockData, setStockData] = useState({})

    // Request the stock information (price, market cap, etc.) and 
    // page info (comments, company bio, likes, etc.) from the server.
    useEffect(() => {
        fetch("/stock_page", {
            method: "POST",
            headers: {
                "content_type":"application/json",
            },
            body: JSON.stringify({stock_id: props.id})
        }
        )
        .then(res => res.json())
        .then(data => {
            setPageData(data['page_data']);
            setStockData(data['stock_data']);
        })
    }, []);

    if ('Name' in stockData) {
        return (
            <div>
                <h1>{stockData['Name']}</h1>
                Following is test data...
                <h1>Comments</h1>
                { 
                    pageData.comments.map((comment) => (
                        <div>
                            {comment.message}
                        </div>
                    ))
                }
                <h1>Company Information</h1>
                {pageData.information}
            </div>
        )
    }

    return (
        <div>
            Loading...
        </div>
    )
}

export default StockPage;