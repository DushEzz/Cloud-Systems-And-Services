CREATE TABLE IF NOT EXISTS counter
(
    id SERIAL PRIMARY KEY,
    requests_count INTEGER DEFAULT 0
);

INSERT INTO counter (id) VALUES (1);