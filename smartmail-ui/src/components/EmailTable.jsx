import React from "react";

function EmailTable({ emails }) {
  return (
    <div className="bg-white shadow rounded-lg p-6 mt-6">
      <h3 className="text-lg font-semibold mb-4">Recent Emails</h3>
      <table className="w-full border-collapse">
        <thead>
          <tr className="bg-gray-100">
            <th className="p-2 border">Sender</th>
            <th className="p-2 border">Subject</th>
            <th className="p-2 border">Status</th>
          </tr>
        </thead>
        <tbody>
          {emails.map((email, index) => (
            <tr key={index} className="text-center">
              <td className="p-2 border">{email.sender}</td>
              <td className="p-2 border">{email.subject}</td>
              <td className={`p-2 border ${email.status === "Safe" ? "text-green-600" : "text-red-600"}`}>
                {email.status}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default EmailTable;
