import './Login.css';
import React from 'react';
import { GoogleLogin } from 'react-google-login';
import { refreshTokenSetup } from '../utils/refreshToken';

const clientId = process.env.REACT_APP_GOOGLE_CLIENT_ID;

function Login(props) {
    
    const onSuccess = (res) => {
        console.log('[Login Success] currentUser: ', res.profileObj);
        var name = res.profileObj.name.split(" ")[0]
        
        props.updateUsername(name);
        props.authenticated();
        
        refreshTokenSetup(res);
    };
    
    const onFailure = (res) => {
        console.log('[Login failed] res: ', res);
    };
    
    return (
        <div className="App-login-button">
            <GoogleLogin
                clientId={clientId}
                buttonText="Login"
                onSuccess={onSuccess}
                onFailure={onFailure}
                cookiePolicy={'single_host_origin'}
                style={{ margin: '0px' }}
                isSignedIn={true}
            />
        </div>
    );
}

export default Login;