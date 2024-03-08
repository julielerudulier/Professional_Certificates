SELECT DISTINCT(name) FROM people, stars, movies
WHERE people.id = stars.person_id
AND stars.movie_id = movies.id
AND movies.year = 2004
ORDER BY people.birth;
