WITH existing_user AS (
    SELECT id
    FROM users
    WHERE email = 'john.doe@example.com'
), inserted_user AS (
    INSERT INTO users (username, email)
        SELECT 'john_doe', 'john.doe@example.com'
        WHERE NOT EXISTS (SELECT 1 FROM existing_user)
        RETURNING id
), final_user AS (
    SELECT id FROM existing_user
    UNION ALL
    SELECT id FROM inserted_user
)

, inserted_bundle AS (
    INSERT INTO bundles (title, description, subject, user_id)
    SELECT 'Sample Bundle', 'This is a sample bundle description', 'Science', id
    FROM final_user
    RETURNING id
)

INSERT INTO cards (term, definition, img, bundle_id)
SELECT 'Term 1', 'Definition of Term 1', 'image_url', id
FROM inserted_bundle;