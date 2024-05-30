CREATE TABLE IF NOT EXISTS users(
    id              UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    username        VARCHAR(255),
    email           VARCHAR(255) UNIQUE
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
    user_id         UUID REFERENCES users(id) NOT NULL,
    bundle_id       UUID REFERENCES bundles(id) NOT NULL
);