import './Login.css';
import React from 'react';
import { GoogleLogin } from 'react-google-login';
import { refreshTokenSetup } from '../utils/refreshToken';

const clientId = process.env.REACT_APP_GOOGLE_CLIENT_ID;

function Login(props) {
    
    const onSuccess = (res) => {
        console.log('[Login Success] currentUser: ', res.profileObj);
        var name = res.profileObj.name.split(" ")[0]
        const email = res.profileObj.email;

        props.updateUsername(name);
        props.authenticated();
        props.setEmail(email);
        refreshTokenSetup(res);

        // Send user data to server
        // to be inserted into DB if a first
        // login is detected
        fetch("/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json; charset=utf-8",
            },
            body: JSON.stringify({email: res.profileObj.email})
        });
    };
    
    const onFailure = (res) => {
        console.log('[Login failed] res: ', res);
    };
    
    return (
        <div className="App-login-button">
            
        </div>
    );
}

export default Login;