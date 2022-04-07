export type Patient = {
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
