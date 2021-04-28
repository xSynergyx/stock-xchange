import React , { useState, useEffect, useRef } from 'react';
import { AiFillLike, AiOutlineLike } from 'react-icons/ai';
import { LikeHandler } from './StockTable.js';
import './StockPage.css';

const StockPage = (props) => {
    const [pageData, setPageData] = useState({})
    const [stockData, setStockData] = useState({})
    const [newsData, setNewsData] = useState([])
    const [activeSection, setActiveSection] = useState('');
    const [isLiked, setLiked] = useState(false);
    const [likedStocks, setLikedStocks] = useState([]);

    // Request the page info (comments, company bio, likes, etc.) from the server.
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

        fetch("/stock_page", {
            method: "POST",
            headers: {
                "Content-Type": "application/json; charset=utf-8",
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

        if (isLiked || likedStocks.filter((stock) => stock.Symbol == props.symbol).length > 0) {
            setLikedStocks((oldStocks) => {
                const newStocks = [...oldStocks];
                return newStocks.filter((stock) => stock.Symbol != props.symbol);
            })
            setLiked(false);
        }
        else {
            setLiked(true);
        }
    }
    
    if ('Error' in stockData) {
        return (
            <div id="page_body">
                <h1>{stockData.Error}</h1>
            </div>
        );
    }

    else if ('Symbol' in stockData) {
        return (
            <div id="page_body">
                <h1>{stockData.Company} ({stockData.Symbol})</h1>
                <h3>Current Price: ${stockData.Price}</h3>
                <h3>High: ${stockData.High}</h3>
                <h3>Low: ${stockData.Low}</h3>
                <h3>Category: {stockData.Category}</h3>
                {isLiked || likedStocks.filter((stock) => stock.Symbol == props.symbol).length > 0 ?
                    <div id="fill_like" onClick={onLike}><AiFillLike size='2em' /></div> :
                    <div id="outline_like" onClick={onLike}><AiOutlineLike size='2em' /></div>
                }
                <div>
                    <button onClick={() => setActiveSection(() => 'News')}>News</button>
                    <button onClick={() => setActiveSection(() => 'Comments')}>Comments</button>
                    <button>Overview</button>
                </div>

                <ContentSection 
                    activeSection={activeSection} 
                    stockData={stockData} 
                    pageData={pageData} 
                    newsData={newsData} 
                    symbol={props.symbol}
                    username={props.username}
                    email={props.email} />
            </div>
        )
    }

    return (
        <div id="page_body">
            Loading...
        </div>
    )
}

const ContentSection = (props) => {
    if (props.activeSection === 'News') {
        if (props.newsData.length > 0 && 'Error' in props.newsData[0]) {
            return (
                <div>
                    {props.newsData[0].Error}
                </div>
            );
        }

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
            <Comments 
                email={props.email}
                symbol={props.symbol}
                username={props.username}
                pageData={props.pageData} />
        );
    }

    else {
        return null;
    }
}

const Comments = (props) => {
    const [comments, setComments] = useState(props.pageData.comments);
    const inputRef = useRef();

    const onSubmitComment = () => {
        if (inputRef.current.value !== '') {
            const comment = inputRef.current.value;
            fetch("/submit_comment", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json; charset=utf-8",
                },
                body: JSON.stringify({comment: comment, email: props.email, stock_symbol: props.symbol})
            });

            setComments((prevComments) => {
                let newComments = [...prevComments];
                newComments.push({username: props.username, stock_symbol: props.symbol, message: comment});
                return newComments;
            });
        }
    }

    return (
        <div>
            {comments.map((comment) => {
                return (
                    <div id="comment">
                        <div id="comment_header">
                            {comment.username} said...
                        </div>
                        <div id="message">
                            {comment.message}
                        </div>
                    </div>
                );
            })}
            <h3>Leave a Comment<br/></h3>
            <input placeholder="Write a comment..." ref={inputRef} type="text" />
            <button type="button" onClick={onSubmitComment}>Submit</button>
        </div>
    );
}

export default StockPage;
