import React, { useState } from 'react';
import axios from 'axios';

const AppointmentForm = () => {
    const [patientName, setPatientName] = useState('');
    const [doctorName, setDoctorName] = useState('');
    const [dateTime, setDateTime] = useState('');
    const [message, setMessage] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();

        const appointmentData = {
            patient: patientName,
            doctor: doctorName,
            date_time: dateTime
        };

        axios.post('http://localhost:8000/api/appointments/', appointmentData)
            .then(response => {
                setMessage('Appointment booked successfully!');
                setPatientName('');
                setDoctorName('');
                setDateTime('');
            })
            .catch(error => {
                setMessage('Error booking appointment. Please try again.');
                console.error('Error:', error);
            });
    };

    return (
        <div>
            <h2>Book Appointment</h2>
            <form onSubmit={handleSubmit}>
                <label>
                    Patient Name:
                    <input type="text" value={patientName} onChange={e => setPatientName(e.target.value)} required />
                </label>
                <br />
                <label>
                    Doctor Name:
                    <input type="text" value={doctorName} onChange={e => setDoctorName(e.target.value)} required />
                </label>
                <br />
                <label>
                    Date & Time:
                    <input type="datetime-local" value={dateTime} onChange={e => setDateTime(e.target.value)} required />
                </label>
                <br />
                <button type="submit">Book Appointment</button>
            </form>
            <p>{message}</p>
        </div>
    );
};

export default AppointmentForm;