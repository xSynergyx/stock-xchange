// import './Profile.css';
// import React from 'react';
import React, { useState } from 'react';
import { socket } from '../App.js';


function UserList() {
    const [userList, SetUserList] = useState([]);

    socket.on('login' , (data) => {
        if(data !== undefined){
            console.log(data);
            SetUserList(prevUserList => prevUserList = data);
        }
    });
    return (
    <div>
        <ul>
            {userList.map((user, index) => (
                <li><p>{user}</p></li>
            ))}
        </ul>
    </div>);
}

export default UserList;