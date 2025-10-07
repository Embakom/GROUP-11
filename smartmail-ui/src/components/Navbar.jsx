import React from "react";

function Navbar() {
  return (
    <div className="bg-white shadow p-4 flex justify-between">
      <h1 className="text-xl font-bold">📧 Smart Mail</h1>
      <button className="bg-blue-600 text-white px-4 py-2 rounded-lg">
        Logout
      </button>
    </div>
  );
}

export default Navbar;
