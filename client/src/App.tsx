import Container from "react-bootstrap/Container";
import Button from "react-bootstrap/Button";
import Col from "react-bootstrap/Col";
import Row from "react-bootstrap/Row";
import { SessionsTable } from "./components";
import { useSessions } from "./hooks";

function App() {
  const { data: sessions, isLoading } = useSessions();

  if (isLoading) {
    return <div>Loading...</div>;
  }

  return (
    <Container style={{ marginTop: "2em" }}>
      <Row>
        <Col sm={10}>
          <h1>Therapy Sessions</h1>
        </Col>
        <Col sm={2}>
          <Button>Add session</Button>
        </Col>
      </Row>
      {sessions && sessions.length ? (
        <SessionsTable sessions={sessions} />
      ) : (
        <div>You have no sessions yet</div>
      )}
    </Container>
  );
}

export default App;
