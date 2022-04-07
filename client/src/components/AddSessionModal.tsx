import { Patient, SessionCreationData } from "../types";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import Modal from "react-bootstrap/Modal";
import { useState } from "react";

type AddSessionModalProps = {
  show: boolean;
  onClose: () => void;
  onSubmit: (values: SessionCreationData) => void;
  patients: Patient[];
};

export function AddSessionModal(props: AddSessionModalProps) {
  const { onClose, onSubmit, show, patients } = props;
  const [values, setValues] = useState<SessionCreationData>({
    fee: 0,
    patient: patients[0],
  });

  return (
    <Modal show={show}>
      <Modal.Header
        closeButton
        onClick={() => {
          onClose();
        }}
      >
        <Modal.Title>Add new session</Modal.Title>
      </Modal.Header>

      <Modal.Body>
        <Form.Group className="mb-3">
          <Form.Group className="mb-3">
            <Form.Label>Patient</Form.Label>
            <Form.Select
              onChange={(e) => {
                setValues((prev) => {
                  const patient = patients.find(
                    ({ id }) => id.toString() === e.target.value
                  );
                  if (patient) return { ...prev, patient };

                  return prev;
                });
              }}
              value={values?.patient.id || patients[0].id}
            >
              {patients.map(({ id, name }) => (
                <option key={id} value={id.toString()}>
                  {name}
                </option>
              ))}
            </Form.Select>
          </Form.Group>
          <Form.Label>Fee</Form.Label>
          <Form.Control
            type="number"
            value={values.fee}
            onChange={(e) => {
              setValues((prev) => ({
                ...prev,
                fee: parseFloat(e.target.value),
              }));
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
            values && onSubmit(values);
          }}
        >
          Submit
        </Button>
      </Modal.Footer>
    </Modal>
  );
}
