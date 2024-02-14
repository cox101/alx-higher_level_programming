-- Lists all shows without the comedy genre in the database hbtn_0d_tvshows.
-- Records are ordered by ascending show title.
SELECT tv_shows.title, COALESCE(SUM(h.rating), 0) AS rating_sum
FROM tv_shows
LEFT JOIN hbtn_0d_tvshows_rate h ON tv_shows.id = h.show_id
GROUP BY tv_shows.id, tv_shows.title
ORDER BY rating_sum DESC;

