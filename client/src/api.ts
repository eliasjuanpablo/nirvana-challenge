import { Session } from "./types";
import axios from "./axios";

export function fetchSessions(): Promise<Session[]> {
  return axios.get("/api/v1/sessions/").then(({ data }) => data);
}
