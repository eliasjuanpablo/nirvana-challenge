import { useQuery, UseQueryResult } from "react-query";
import { fetchSessions } from "../api";
import { Session } from "../types";

export function useSessions(): UseQueryResult<Session[], Error> {
  return useQuery("fetchSessions", fetchSessions);
}
