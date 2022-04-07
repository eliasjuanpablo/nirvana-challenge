import {
  useMutation,
  UseMutationResult,
  useQuery,
  UseQueryResult,
} from "react-query";
import { addPayment, addSession, fetchPatients, fetchSessions } from "../api";
import { Patient, Payment, Session } from "../types";

export function useSessions(): UseQueryResult<Session[], Error> {
  return useQuery("fetchSessions", fetchSessions, { cacheTime: 0 });
}

export function usePatients(): UseQueryResult<Patient[], Error> {
  return useQuery("fetchPatients", fetchPatients);
}

export function useAddSession(): UseMutationResult<Session, Error> {
  return useMutation((payload: any) => addSession(payload));
}

export function useAddPayment(): UseMutationResult<Payment, Error> {
  return useMutation((payload: any) => addPayment(payload));
}
