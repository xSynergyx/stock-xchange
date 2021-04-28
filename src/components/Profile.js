import './Profile.css';
import React, { useState } from 'react';
import { MdEdit } from 'react-icons/md';

function Profile(props) { // Have to get the username and bio from the DB
    return (
        <div className="grid-container">
            <div className="personal">
                <h1>Profile</h1>
                <div><p>Name: { props.username } <MdEdit /></p> </div>
                <p>Username: { props.email } <MdEdit /></p> 
                <p>Bio: <MdEdit /></p>
            </div>
            <div className="favorites">
                <h1>Some Profile Thing(?)</h1>
                <p>Thought it was gonna be stocks here. Going to have to change it</p>
            </div>
            <div className="investor-preferences">
                <h1>Investing Style</h1>
                <p>Preferred stock information</p>
            </div>
        </div>);
}

export default Profile;