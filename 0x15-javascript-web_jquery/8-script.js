$(document).ready(function() {
    $.ajax({
        url: "https://swapi-api.alx-tools.com/api/films/?format=json",
        method: "GET",
        success: function(data) {
            var movies = data.results;
            var list = $("UL#list_movies");
            $.each(movies, function(index, movie) {
                list.append("<li>" + movie.title + "</li>");
            });
        },
        error: function(xhr, status, error) {
            console.error("Error fetching movie titles:", error);
        }
    });
});

