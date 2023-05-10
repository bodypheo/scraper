CREATE TABLE urls(
    url_id INTEGER NOT NULL PRIMARY KEY,
    url VARCHAR,
    nombre_app VARCHAR,
    date_db DATETIME,
    date_update DATE,
    date_launch DATE,
    last_visited DATE,
    downloads INTEGER,
    description VARCHAR,
    num_reviews INTEGER,
    rate FLOAT
)