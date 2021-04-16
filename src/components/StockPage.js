import React , { useState, useEffect } from 'react';
import './StockPage.css';

const StockPage = (props) => {
    const [pageData, setPageData] = useState({})
    const [stockData, setStockData] = useState({})
    const [newsData, setNewsData] = useState([])
    const [activeSection, setActiveSection] = useState('');

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
            setNewsData(data['news_data']);
        })
    }, [props.symbol]);

    if ('Symbol' in stockData) {
        return (
            <div id="page_body">
                <h1>{stockData.Company} ({stockData.Symbol})</h1>
                <h3>Current Price: ${stockData.Price}</h3>
                <h3>High: ${stockData.High}</h3>
                <h3>Low: ${stockData.Low}</h3>
                <h3>Category: {stockData.Category}</h3>
                
                <div>
                    <button onClick={() => setActiveSection(() => 'News')}>News</button>
                    <button onClick={() => setActiveSection(() => 'Comments')}>Comments</button>
                    <button>Overview</button>
                </div>

                <ContentSection 
                    activeSection={activeSection} 
                    stockData={stockData} 
                    pageData={pageData} 
                    newsData={newsData} />
            </div>
        )
    }

    return (
        <div>
            Loading...
        </div>
    )
}

const ContentSection = (props) => {
    if (props.activeSection === 'News') {
        return (
            <div>
                {props.newsData.map((article) => {
                    return (
                        <div>
                            <h2>{article.headline}</h2>
                            {article.snippet.length === 0 ? <h3>No Snippet Available</h3> : <h3>{article.snippet}</h3>}
                        </div>
                    );
                })}
            </div>
        );
    }
    else if (props.activeSection === 'Comments') {
        return (
            <div>
                {props.pageData.comments.map((comment) => {
                    return (
                        <div>
                            {comment.message}
                        </div>
                    );
                })}
            </div>
        );
    }

    else {
        return null;
    }
}

export default StockPage;