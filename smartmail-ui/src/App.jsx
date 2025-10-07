import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Sidebar from './components/Sidebar';
import Dashboard from './pages/Dashboard';
import Inbox from './pages/Inbox';
import Sent from './pages/Sent';

function App() {
  return (
    <Router>
      <div className="flex h-screen">
        <Sidebar />
        <div className="flex-1 p-4 bg-gray-100">
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/inbox" element={<Inbox />} />
            <Route path="/sent" element={<Sent />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
