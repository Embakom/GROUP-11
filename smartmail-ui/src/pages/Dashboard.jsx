import React from "react";
import DashboardCard from "../components/DashboardCard";
import EmailTable from "../components/EmailTable";

function Dashboard() {
  const emails = [
    { sender: "admin@gmail.com", subject: "Welcome!", status: "Safe" },
    { sender: "unknown@phish.com", subject: "Reset password", status: "Phishing" }
  ];

  return (
    <div>
      <h2 className="text-2xl font-bold mb-6">Dashboard</h2>
      <div className="grid grid-cols-3 gap-6">
        <DashboardCard title="Total Emails Scanned" value="120" />
        <DashboardCard title="Safe Emails" value="100" />
        <DashboardCard title="Threats Found" value="20" />
      </div>
      <EmailTable emails={emails} />
    </div>
  );
}

export default Dashboard;
