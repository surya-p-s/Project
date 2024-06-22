import React, { useState, useEffect } from 'react';
import axios from 'axios';

const TreatmentPlans = () => {
    const [treatmentPlans, setTreatmentPlans] = useState([]);

    useEffect(() => {
        // Fetch treatment plans from backend API
        axios.get('http://localhost:8000/api/treatment-plans/')
            .then(response => {
                setTreatmentPlans(response.data);
            })
            .catch(error => {
                console.error('Error fetching treatment plans:', error);
            });
    }, []);

    return (
        <div>
            <h2>Treatment Plans</h2>
            <ul>
                {treatmentPlans.map(plan => (
                    <li key={plan.id}>
                        <strong>{plan.patient.name}</strong> - {plan.description}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default TreatmentPlans;
