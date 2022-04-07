import { Session } from "./types";

export function fetchSessions(): Promise<Session[]> {
  return Promise.resolve([
    {
      id: 1,
      patient: { name: "John Doe", email: "test@test.com" },
      fee: 200,
      date: new Date(),
    },
  ]);
}
