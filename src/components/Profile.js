import './Profile.css';
import React, { useState } from 'react';
import { MdEdit } from 'react-icons/md';

function Profile(props) { // Have to get the username and bio from the DB
    return (
        <div className="grid-container">
            <div className="personal">
                <h2 className="profile-title">Profile</h2>
                <p>Name: { props.username } <MdEdit /></p>
                <p>Username: { props.email }</p> 
                <p>Bio: I like stocks <MdEdit /></p>
            </div>
            <div className="favorites">
                <h2 className="profile-title">Some Profile Thing(?)</h2>
                <p>Thought it was gonna be stocks here. Going to have to change it</p>
            </div>
            <div className="investor-preferences">
                <h2 className="profile-title">Investing Style</h2>
                <p>Preferred stock information</p>
            </div>
        </div>);
}

export default Profile;