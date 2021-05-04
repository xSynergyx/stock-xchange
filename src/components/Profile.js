import './Profile.css';
import React, { useState, useEffect } from 'react';
import { MdEdit } from 'react-icons/md';

function Profile(props) { // Have to get the username and bio from the DB

    const [userBio, setUserBio] = useState("");
    /*
    function clickEdit(){
        alert('Clicked edit button');
    }*/

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
    }, []);
    return (
        <div className="grid-container">
            <div className="personal">
                <h2 className="profile-title">Profile</h2>
                <p>Name: { props.username } <MdEdit /></p>
                <p>Username: { props.email }</p> 
                <p>Bio: { userBio } <MdEdit /></p>
            </div>
            <div className="favorites">
                <h2 className="profile-title">Investing Style</h2>
                <p>Preferred stock information</p>
            </div>
            <div className="investor-preferences">
                <h2 className="profile-title">Settings</h2>
                <p>Profile visibility</p>
            </div>
        </div>);
}

export default Profile;