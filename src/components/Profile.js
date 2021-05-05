import './Profile.css';
import React, { useState, useEffect } from 'react';
import { MdEdit } from 'react-icons/md';
import { IconContext } from "react-icons";
import BioInput from './BioInput.js';

function Profile(props) { // Have to get the username and bio from the DB

    const [userBio, setUserBio] = useState("");
    const [editBio, setEditBio] = useState(false);
    
    
    function clickEdit(){
        setEditBio(true);
    }

    useEffect(() => {
        fetch("/get_user_profile", {
            method: "POST",
            headers: {
                "Content-Type": "application/json; charset=utf-8",
            },
            body: JSON.stringify({email: props.email})
        })
        .then(res => res.json())
        .then(data => {
            setUserBio(data.Bio);
        });
    }, [editBio]);
    
    return (
        <div className="grid-container">
            <div className="personal">
                <h2 className="profile-title">Profile</h2>
                <h2 className="profile-sections">Name </h2>
                <p>{ props.username }</p>
                <h2 className="profile-sections">Username</h2>
                <p>{ props.email }</p>
                <h2 className="profile-sections">Bio</h2>
                <IconContext.Provider value={{ color: "green", className: "edit-icon" }}>
                <p>
                    { editBio ? <BioInput userBio={userBio} setEditBio={setEditBio} email={props.email}/>
                            : <div>{userBio} <MdEdit onClick={ clickEdit }/></div>
                    }
                </p>
                </IconContext.Provider>
                
            </div>
            <div className="favorites">
                <h2 className="profile-title">Investing Style</h2>
                <p>Coming soon</p>
            </div>
            <div className="investor-preferences">
                <h2 className="profile-title">Settings</h2>
                <p>Profile visibility</p>
            </div>
        </div>);
}

export default Profile;