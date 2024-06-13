INSERT INTO users (email, password, created_at) VALUES
    ('user@mail.com', '$2y$10$br4FGaTysyQI7ZyHc6MDuuWPg2ZC/LsT89yYi.Dzjl2GYZT48UWKO', NOW()),
    ('admin@mail.com', '$2y$10$uRUfUquE8bRNcaGWo4DwqOTTfbqEGybGoF8WcOtVhaPfNESzXCdyG', NOW());

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