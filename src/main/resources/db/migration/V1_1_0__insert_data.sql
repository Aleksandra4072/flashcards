INSERT INTO users (email, password) VALUES
    ('user@mail.com', '$2a$12$zbsZnJO.L4BTTG2J9RlN7uhIZ6wKRJJ8IgB2pEuqiR5t0/SOkHcj.'),
    ('admin@mail.com', '$2a$12$6NXLs611NkZ7HMJQKLUbOeTI70ecRttyiykp/KXocyHZz3eXfQIZK');

-- create roles
INSERT INTO roles (name, description) VALUES
    ('ROLE_ADMIN', 'Administrator role with all privileges'),
    ('ROLE_USER', 'Regular user role with limited privileges');


INSERT INTO user_roles (user_id, role_id)
SELECT users.id, roles.id
FROM users, roles
WHERE users.email = 'admin@mail.com' AND roles.name IN ('ROLE_ADMIN', 'ROLE_USER');


INSERT INTO user_roles (user_id, role_id)
SELECT users.id, roles.id
FROM users, roles
WHERE users.email = 'user@mail.com' AND roles.name = 'ROLE_USER';



INSERT INTO bundles (title, description, subject, user_id)
SELECT 'Sample Bundle', 'This is a sample bundle description', 'Science', users.id
FROM users
WHERE users.email = 'user@mail.com';


-- Insert cards
INSERT INTO cards (term, definition, img, bundle_id)
SELECT 'Term 1', 'Definition of Term 1', 'image_url', bundles.id
FROM bundles
WHERE bundles.title = 'Sample Bundle';

-- yCAv3wLqePVt24DQJzhgHj : admin
-- Ljh4rqEGA9YVbve8MtzDFf : user