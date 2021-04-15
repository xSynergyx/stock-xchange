import React , { useState, useEffect } from 'react';

const StockPage = (props) => {
    const [pageData, setPageData] = useState({})
    const [stockData, setStockData] = useState({})

    // Request the page info (comments, company bio, likes, etc.) from the server.
    useEffect(() => {
        fetch("/stock_page", {
            method: "POST",
            headers: {
                "content_type":"application/json",
            },
            body: JSON.stringify({stock_symbol: props.symbol})
        })
        .then(res => res.json())
        .then(data => {
            setPageData(data['page_data']);
            setStockData(data['stock_data']);
        })
    }, []);

    if ('Symbol' in stockData) {
        return (
            <div>
                <h1>{stockData['Company']}</h1>
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