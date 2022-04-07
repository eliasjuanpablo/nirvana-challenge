import { Patient, Session, SessionCreationData } from "./types";
import axios from "./axios";

export function fetchSessions(): Promise<Session[]> {
  return axios.get("/api/v1/sessions/").then(({ data }) => data);
}

export function fetchPatients(): Promise<Patient[]> {
  return axios.get("/api/v1/patients/").then(({ data }) => data);
}

export function addSession(payload: SessionCreationData): Promise<Session> {
  return axios
    .post("/api/v1/sessions/", {
      ...payload,
      patient_id: payload.patient.id,
    })
    .then(({ data }) => data);
}
