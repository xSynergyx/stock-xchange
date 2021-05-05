import './BioInput.css';
import React, { useState } from 'react';

function BioInput(props) {
    // Text typed in by the user
    const [updateBio, setUpdateBio] = useState("");
    
    // Update bio after user submits
    function handleSubmit(event){
        event.preventDefault();
        console.log(updateBio);
        props.setEditBio(false);
        
        fetch("/update_bio", {
            method: "POST",
            headers: {
                "Content-Type": "application/json; charset=utf-8",
            },
            body: JSON.stringify({email: props.email, newBio: updateBio})
        });
    }

    return (
        <form onSubmit={ handleSubmit }>
            <input 
            id="bio_input"
            type="text" 
            placeholder={ props.userBio } 
            onChange={(e) => setUpdateBio(e.target.value)} />
            <input type="submit" value="Save" />
        </form>
    );
}

export default BioInput;