import Container from "react-bootstrap/Container";
import { SessionsTable } from "./components";
import { useSessions } from "./hooks";

function App() {
  const { data: sessions } = useSessions();

  return (
    <Container>
      {sessions && sessions.length ? (
        <SessionsTable sessions={sessions} />
      ) : (
        <div>You have no sessions yet</div>
      )}
    </Container>
  );
}

export default App;
