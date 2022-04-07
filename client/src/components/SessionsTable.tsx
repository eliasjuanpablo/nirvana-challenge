import { Button } from "react-bootstrap";
import Table from "react-bootstrap/Table";

import { Session } from "../types";

type SessionsTableProps = {
  sessions: Session[];
};

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
        {sessions.map(({ date, patient, fee }, index) => {
          return (
            <tr key={index}>
              <td>{date.toISOString()}</td>
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
