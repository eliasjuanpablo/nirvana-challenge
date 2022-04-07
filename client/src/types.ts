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
  date: Date;
  patient: Patient;
  fee: number;
};
