import {
  useMutation,
  UseMutationResult,
  useQuery,
  UseQueryResult,
} from "react-query";
import { addSession, fetchPatients, fetchSessions } from "../api";
import { Patient, Session } from "../types";

export function useSessions(): UseQueryResult<Session[], Error> {
  return useQuery("fetchSessions", fetchSessions);
}

export function usePatients(): UseQueryResult<Patient[], Error> {
  return useQuery("fetchPatients", fetchPatients);
}

export function useAddSession(): UseMutationResult<Session, Error> {
  return useMutation((payload: any) => addSession(payload));
}
