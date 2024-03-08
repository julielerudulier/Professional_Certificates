SELECT title FROM movies, stars, people, ratings
WHERE people.name = 'Chadwick Boseman'
AND stars.person_id = people.id
AND ratings.movie_id = stars.movie_id
AND movies.id = ratings.movie_id
ORDER BY ratings.rating DESC
LIMIT 5;
