// import './Profile.css';
// import React from 'react';
import React, { useState } from 'react';
import { socket } from '../App.js';


function UserList() {
    const [usersList, setUserList] = useState(["User 12"]);
    

    socket.on('login' , (data) => { // [array of users]
        if(data !== undefined){
            console.log(data);
            setUserList(prevUser => {
                prevUser = data;
            });
            // data.map((user) => console.log(user));
        }
    });

    
    // console.log(usersList)
    return (
    <div>
        <ul>
            {usersList.map((user, index) => 
                <li>{ user }</li>
            )}
        </ul>
    </div>
    );
}

export default UserList;