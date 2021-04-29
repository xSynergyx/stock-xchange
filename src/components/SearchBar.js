import './SearchBar.css';
import React, { useState } from 'react';
import { useHistory } from "react-router-dom";

function SearchBar() {
    // Text typed in by the user
    const [searchText, setSearchText] = useState("");
    const history = useHistory();

    // Search for stock after user submission
    function handleSubmit(event){
        event.preventDefault();
        console.log(searchText);
        history.push('/stock_page/' + searchText);
    }

    return (
        <form onSubmit={ handleSubmit }>
            <input 
            id="search_box"
            type="text" 
            placeholder="Search stocks" 
            onChange={(e) => setSearchText(e.target.value)} />
        </form>
    );
}

export default SearchBar;