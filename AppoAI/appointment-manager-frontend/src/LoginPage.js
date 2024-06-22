import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const LoginPage = () => {
    const [role, setRole] = useState('patient');
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [message, setMessage] = useState('');
    const navigate = useNavigate();

    const handleRoleChange = (e) => {
        setRole(e.target.value);
        setMessage('');
    };

    const handleLogin = (e) => {
        e.preventDefault();

        const loginData = {
            username: username,
            password: password
        };

        const url = role === 'patient'
            ? 'http://localhost:8000/api/patient-login/'
            : 'http://localhost:8000/api/doctor-login/';

        axios.post(url, loginData)
            .then(response => {
                localStorage.setItem('token', response.data.token);
                setMessage(`Login successful! Welcome ${role}`);
                navigate(`/${role}-dashboard`);
            })
            .catch(error => {
                setMessage('Invalid username or password. Please try again.');
                console.error('Error:', error);
            });
    };

    return (
        <div>
            <h2>Login</h2>
            <form onSubmit={handleLogin}>
                <div>
                    <label>
                        Role:
                        <select value={role} onChange={handleRoleChange}>
                            <option value="patient">Patient</option>
                            <option value="doctor">Doctor</option>
                        </select>
                    </label>
                </div>
                <div>
                    <label>
                        Username:
                        <input
                            type="text"
                            value={username}
                            onChange={(e) => setUsername(e.target.value)}
                            required
                        />
                    </label>
                </div>
                <div>
                    <label>
                        Password:
                        <input
                            type="password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            required
                        />
                    </label>
                </div>
                <button type="submit">Login</button>
            </form>
            <p>{message}</p>
        </div>
    );
};

export default LoginPage;
