import Container from "react-bootstrap/Container";
import Button from "react-bootstrap/Button";
import Col from "react-bootstrap/Col";
import Row from "react-bootstrap/Row";

import { AddSessionModal, SessionsTable } from "./components";
import { useAddSession, usePatients, useSessions } from "./hooks";
import { useEffect, useState } from "react";
import { SessionCreationData } from "./types";

function App() {
  const {
    data: sessions,
    isLoading: isLoadingSessions,
    refetch: refetchSessions,
  } = useSessions();
  const { data: patients } = usePatients();
  const { mutate: addSession, isSuccess: isSessionAdded } = useAddSession();
  const [showAddModal, setShowAddModal] = useState(false);

  useEffect(() => {
    setShowAddModal(false);
    refetchSessions();
  }, [isSessionAdded, refetchSessions]);

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
          <SessionsTable sessions={sessions} />
        ) : (
          <div>You have no sessions yet</div>
        )}
      </Container>
    </>
  );
}

export default App;
