Database Design (PostgreSQL)

You should have:

students

- id (PK)
- name
- email

clubs

- id (PK)
- name
- description

memberships

- id (PK)
- student_id (FK)
- club_id (FK)
