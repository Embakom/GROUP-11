import React from "react";

function DashboardCard({ title, value }) {
  return (
    <div className="bg-white shadow rounded-lg p-6 text-center">
      <h3 className="text-lg font-semibold">{title}</h3>
      <p className="text-2xl font-bold text-blue-600">{value}</p>
    </div>
  );
}

export default DashboardCard;
