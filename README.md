## Nirvana challenge

A therapy sessions + payments tracker

### Setup

Using docker:

`$ docker-compose up --build`

Run DB migrations:

`$ docker-compose exec server python3 manage.py migrate`

    NOTE: migrations include seeding so that entities are ready to be used

Open frontend:

`http://localhost:3000`

### Overview

This project was implemented using Django and React (TS). It includes design decisions such as:

- Views (i.e. Django's "Controllers") are fairly thin. They are meant to:

  - Validate incoming JSON payloads' shape
  - Delegate domain logic handling to models
  - Serialize results and send JSON responses

- Models and Domain logic tend to be coupled in Django projects, as the framework itself relies on them heavily.

- Views handle validation and domain exceptions, and turn them into HTTP 4xx errors.

- The domain logic has been implemented in an inside-out fashion (i.e. testing the interaction between models before exposing HTTP endpoints).

- SQLite was used for simplicity.

- React components were written as functions.

- React Query was meant to simplify loading states, refetching and error handling. However the implementation is not finished and it may seem kind of bloated.

- Bootstrap was used for simplicity sake.

### Things I would have added with more time

- Validation is happening in the backend but not being handled in the frontend. This prevents invalid state in the server, but still exposes a clunky UX.

- Loading spinners could be added by leveraging react query.

- Fully paid sessions could have been shown on the sessions table. It could be easily annotated to the sessions endpoint response by aggregating all the preexisting payments.

- Frontend tests could have been added by using React Testing Library.

- Dockerfiles are for development purposes and are not meant to be deployable.

- The frontend is not responsive.

- There might be some wild `any` types here and there where for some reason react query was not working as expected.
