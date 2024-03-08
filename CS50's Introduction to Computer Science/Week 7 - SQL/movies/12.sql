SELECT title
FROM movies
    INNER JOIN stars ON stars.movie_id = movies.id
    INNER JOIN people ON stars.person_id = people.id
WHERE people.name IN ('Bradley Cooper', 'Jennifer Lawrence')
GROUP BY movies.title
HAVING count(movies.id) > 1;
