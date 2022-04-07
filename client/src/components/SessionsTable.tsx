import { Button } from "react-bootstrap";
import Table from "react-bootstrap/Table";

import { Session } from "../types";
import { formatDate } from "../utils";

type SessionsTableProps = {
  sessions: Session[];
  onAddPayment: (session: Session) => void;
};

export function SessionsTable(props: SessionsTableProps) {
  const { sessions, onAddPayment } = props;

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
        {sessions.map((session, index) => {
          const { created_at, patient, fee } = session;
          return (
            <tr key={index}>
              <td>{formatDate(created_at)}</td>
              <td>{patient.name}</td>
              <td>{fee}</td>
              <td>
                <Button
                  variant="primary"
                  onClick={() => {
                    onAddPayment(session);
                  }}
                >
                  Add payment
                </Button>
              </td>
            </tr>
          );
        })}
      </tbody>
    </Table>
  );
}
