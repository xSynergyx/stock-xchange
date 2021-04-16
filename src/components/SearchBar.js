import './SearchBar.css';
import React, { useState } from 'react';

function SearchBar() {
    
    // Text typed in by the user
    const [searchText, setSearchText] = useState("");
    
    // Search for stock after user submission
    function handleSubmit(event){
        event.preventDefault();
        console.log("Running doSomething function");
        console.log(searchText);
        
        // TODO: run stock look-up calls in here using searchText
    }
    
    return (
        <form onSubmit={ handleSubmit }>
            <input type="text" 
            placeholder="Search stocks" 
            onChange={(e) => setSearchText(e.target.value)} />
        </form>
        );
}

export default SearchBar;