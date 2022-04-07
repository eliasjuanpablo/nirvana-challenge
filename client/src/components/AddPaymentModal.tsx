import { Session } from "../types";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import Modal from "react-bootstrap/Modal";
import { useState } from "react";
import { formatDate } from "../utils";

type AddPaymentModalProps = {
  show: boolean;
  onClose: () => void;
  onSubmit: (amount: number) => void;
  session: Session;
};

export function AddPaymentModal(props: AddPaymentModalProps) {
  const { onClose, onSubmit, show, session } = props;
  const [amount, setAmount] = useState(0);

  return (
    <Modal show={show}>
      <Modal.Header
        closeButton
        onClick={() => {
          onClose();
        }}
      >
        <Modal.Title>Add payment</Modal.Title>
      </Modal.Header>

      <Modal.Body>
        <Form.Group className="mb-3">
          <Form.Label>Patient</Form.Label>
          <Form.Control disabled value={session.patient.name} />
        </Form.Group>
        <Form.Group className="mb-3">
          <Form.Label>Session date</Form.Label>
          <Form.Control disabled value={formatDate(session.created_at)} />
        </Form.Group>
        <Form.Group className="mb-3">
          <Form.Label>Amount</Form.Label>
          <Form.Control
            type="number"
            value={amount}
            onChange={(e) => {
              setAmount(parseFloat(e.target.value));
            }}
          />
        </Form.Group>
      </Modal.Body>
      <Modal.Footer>
        <Button
          variant="secondary"
          onClick={() => {
            onClose();
          }}
        >
          Close
        </Button>
        <Button
          variant="primary"
          onClick={() => {
            onSubmit(amount);
          }}
        >
          Submit
        </Button>
      </Modal.Footer>
    </Modal>
  );
}
