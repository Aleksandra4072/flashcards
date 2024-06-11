CREATE TABLE IF NOT EXISTS users(
    id              UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    email           VARCHAR(255) UNIQUE,
    password        VARCHAR(255),
    created_at      DATE DEFAULT CURRENT_DATE NOT NULL,
    updated_at      DATE NULL
);

CREATE TABLE IF NOT EXISTS bundles(
    id              UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    title           VARCHAR(255),
    description     TEXT,
    subject         VARCHAR(100),
    user_id         UUID REFERENCES users(id) NOT NULL
);

CREATE TABLE IF NOT EXISTS cards(
    id              UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    term            VARCHAR(255) NOT NULL,
    definition      TEXT NOT NULL,
    img             VARCHAR(255),
    bundle_id       UUID REFERENCES bundles(id) NOT NULL
);