import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Appointments = () => {
    const [appointments, setAppointments] = useState([]);

    useEffect(() => {
        // Fetch appointments from backend API
        axios.get('http://localhost:8000/api/appointments/')
            .then(response => {
                setAppointments(response.data);
            })
            .catch(error => {
                console.error('Error fetching appointments:', error);
            });
    }, []);

    return (
        <div>
            <h2>Appointments</h2>
            <ul>
                {appointments.map(appointment => (
                    <li key={appointment.id}>
                        <strong>{appointment.patient.name}</strong> - {appointment.date_time}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Appointments;
