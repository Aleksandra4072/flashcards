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

CREATE TABLE IF NOT EXISTS roles(
    id              UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    name            VARCHAR(255) NOT NULL,
    description     VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS user_roles(
    user_id        UUID REFERENCES users(id) NOT NULL,
    role_id        UUID REFERENCES roles(id) NOT NULL,
    PRIMARY KEY (user_id, role_id)
);

CREATE TABLE IF NOT EXISTS refresh_tokens(
    id              UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    token           VARCHAR,
    expiry_date     TIMESTAMP WITH TIME ZONE NOT NULL,
    user_id         UUID REFERENCES users(id) NOT NULL UNIQUE
);