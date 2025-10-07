import React from 'react';
import { Link } from 'react-router-dom';

function Sidebar() {
  return (
    <div className="w-64 bg-white border-r p-4">
      <h2 className="text-2xl font-bold mb-6">SmartMail</h2>
      <nav className="flex flex-col gap-4">
        <Link className="hover:text-blue-500" to="/">Dashboard</Link>
        <Link className="hover:text-blue-500" to="/inbox">Inbox</Link>
        <Link className="hover:text-blue-500" to="/sent">Sent</Link>
      </nav>
    </div>
  );
}

export default Sidebar;
