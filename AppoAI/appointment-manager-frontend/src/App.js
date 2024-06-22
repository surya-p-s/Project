import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import logo from './logo1.svg';
import './App.css';
import LoginPage from './LoginPage';
import PatientDashboard from './PatientDashboard';
import DoctorDashboard from './DoctorDashboard';
import ProtectedRoute from './ProtectedRoute';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Health Ease</h1>
        <img src={logo} className="App-logo" alt="logo" />
      </header>
      <main className="App-main">
        <div className="App-content">
          {/* <LoginPage /> */}
                    {/* <PatientDashboard />
                    <DoctorDashboard /> */}
                    {/* Add other components here */}
          <Router>
            <Routes>
                <Route path="/" element={<LoginPage />} />
                <Route path="/patient-dashboard" element={<ProtectedRoute component={PatientDashboard} role="patient" />} />
                <Route path="/doctor-dashboard" element={<ProtectedRoute component={DoctorDashboard} role="doctor" />} />
            </Routes>
        </Router>
        </div>       
      </main>
    </div>
  );
}

export default App;
