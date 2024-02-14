-- Lists all genres in the database hbtn_0d_tvshows_rate by their rating.
-- Records are ordered by descending rating.
SELECT tv_genres.name, COALESCE(SUM(h.rating), 0) AS rating_sum
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
LEFT JOIN hbtn_0d_tvshows_rate h ON tv_shows.id = h.show_id
GROUP BY tv_genres.id, tv_genres.name
ORDER BY rating_sum DESC;

