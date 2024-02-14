-- Lists all genres of the database hbtn_0d_tvshows
-- not linked to the show Dexter.
-- Records are sorted by ascending genre name.
SELECT tv_genres.name
FROM tv_genres
LEFT JOIN (
    SELECT tv_genres.id
    FROM tv_genres
    JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
    JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
    WHERE tv_shows.title = 'Dexter'
) AS DexterGenres ON tv_genres.id = DexterGenres.id
WHERE DexterGenres.id IS NULL
ORDER BY tv_genres.name ASC;

