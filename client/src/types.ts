export type Patient = {
  id: number;
  name: string;
  email: string;
};

export type Therapist = {
  name: string;
  email: string;
};

export type Session = {
  id: number;
  created_at: string;
  patient: Patient;
  fee: number;
};

export type SessionCreationData = Pick<Session, "fee" | "patient">;
