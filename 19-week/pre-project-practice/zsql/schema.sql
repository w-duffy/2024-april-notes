CREATE TABLE actors (
    id INTEGER PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INTEGER,
    bio VARCHAR(2000)
);


CREATE TABLE movies (
    id INTEGER PRIMARY KEY,
    title VARCHAR(50) NOT NULL,
    year INTEGER
);

CREATE TABLE movie_actors (
    actor_id INTEGER,
    movie_id INTEGER,
    PRIMARY KEY (actor_id, movie_id),
    FOREIGN KEY (actor_id) REFERENCES actors(id),
    FOREIGN KEY (movie_id) REFERENCES movies(id)
);


SELECT a.id, a.name, a.age, a.bio
FROM actors a
JOIN movie_actors ma ON a.id = ma.actor_id
JOIN movies m ON m.id = ma.movie_id
WHERE m.id = 1;
