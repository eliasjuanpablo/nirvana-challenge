import Container from "react-bootstrap/Container";
import Button from "react-bootstrap/Button";
import Col from "react-bootstrap/Col";
import Row from "react-bootstrap/Row";

import { AddPaymentModal, AddSessionModal, SessionsTable } from "./components";
import {
  useAddPayment,
  useAddSession,
  usePatients,
  useSessions,
} from "./hooks";
import { useEffect, useState } from "react";
import { Session, SessionCreationData } from "./types";

function App() {
  const {
    data: sessions,
    isLoading: isLoadingSessions,
    refetch: refetchSessions,
  } = useSessions();
  const { data: patients } = usePatients();
  const { mutate: addSession, isSuccess: isSessionAdded } = useAddSession();
  const [showAddModal, setShowAddModal] = useState(false);
  const [selectedSession, setSelectedSession] = useState<Session | null>(null);
  const { mutate: addPayment, isSuccess: isPaymentAdded } = useAddPayment();

  useEffect(() => {
    setShowAddModal(false);
    setSelectedSession(null);
    refetchSessions();
  }, [isSessionAdded, isPaymentAdded, refetchSessions]);

  if (isLoadingSessions) {
    return <div>Loading...</div>;
  }

  return (
    <>
      <AddSessionModal
        show={showAddModal}
        onClose={() => {
          setShowAddModal(false);
        }}
        onSubmit={(values: SessionCreationData) => {
          addSession(values);
        }}
        patients={patients || []}
      />
      {selectedSession && (
        <AddPaymentModal
          show={true}
          onClose={() => {
            setSelectedSession(null);
          }}
          onSubmit={(amount) => {
            selectedSession !== null &&
              addPayment({ session: selectedSession.id, amount });
          }}
          session={selectedSession}
        />
      )}
      <Container style={{ marginTop: "2em" }}>
        <Row>
          <Col sm={10}>
            <h1>Therapy Sessions</h1>
          </Col>
          <Col sm={2}>
            <Button
              onClick={() => {
                setShowAddModal(true);
              }}
            >
              Add session
            </Button>
          </Col>
        </Row>
        {sessions?.length ? (
          <SessionsTable
            sessions={sessions}
            onAddPayment={(session) => {
              setSelectedSession(session);
            }}
          />
        ) : (
          <div>You have no sessions yet</div>
        )}
      </Container>
    </>
  );
}

export default App;
