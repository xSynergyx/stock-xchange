import './Login.css';
import React from 'react';
import { GoogleLogout } from 'react-google-login';

//might still need to require dotenv. Check again in an hour
//require('dotenv').config()

const clientId = process.env.REACT_APP_GOOGLE_CLIENT_ID;
console.log(process.env);

function Logout(props) {
    
    const onSuccess = (res) => {
        alert('Logout made successfully');
        props.authenticated();
    };
    
    return (
        <div>
            <GoogleLogout
                clientId={clientId}
                buttonText="Logout"
                onLogoutSuccess={onSuccess}
            ></GoogleLogout>
        </div>
        );
}

export default Logout;