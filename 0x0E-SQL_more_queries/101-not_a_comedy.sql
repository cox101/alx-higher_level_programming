-- Lists all shows without the comedy genre in the database hbtn_0d_tvshows.
-- Records are ordered by ascending show title.
SELECT tv_shows.title
FROM tv_shows
LEFT JOIN (
    SELECT tv_show_genres.show_id
    FROM tv_show_genres
    JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
    WHERE tv_genres.name = 'Comedy'
) AS ComedyShows ON tv_shows.id = ComedyShows.show_id
WHERE ComedyShows.show_id IS NULL
ORDER BY tv_shows.title ASC;

