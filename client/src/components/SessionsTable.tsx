import { Button } from "react-bootstrap";
import Table from "react-bootstrap/Table";

import { Session } from "../types";

type SessionsTableProps = {
  sessions: Session[];
};

function formatDate(date: string): string {
  const dateInstance = new Date(date);
  return dateInstance.toISOString().substring(0, 10);
}

export function SessionsTable(props: SessionsTableProps) {
  const { sessions } = props;

  return (
    <Table striped bordered hover>
      <thead>
        <tr>
          <th>Date</th>
          <th>Patient</th>
          <th>Fee</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        {sessions.map(({ created_at, patient, fee }, index) => {
          return (
            <tr key={index}>
              <td>{formatDate(created_at)}</td>
              <td>{patient.name}</td>
              <td>{fee}</td>
              <td>
                <Button variant="primary">Add payment</Button>
              </td>
            </tr>
          );
        })}
      </tbody>
    </Table>
  );
}
