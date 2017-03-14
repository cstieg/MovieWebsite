"""Creates a webpage showing favorite movies from a list of movie objects
"""

from fresh_tomatoes import open_movies_page

class Movie(object): # pylint: disable=too-few-public-methods
    """A class containing the attributes of a movie, including links to a
    poster image and youtube trailer"""
    def __init__(self, title, description, img_url, trailer_url):
        self.title = title
        self.description = description
        self.poster_image_url = img_url
        self.trailer_youtube_url = trailer_url

def main():
    """Creates an array and appends Movie class instances to it, then creates
    an HTML page using the open_movies_page function"""
    movies = []
    movies.append(Movie("The Prestige",
                        "Two English magicians duel to create the greatest magic show",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA4NDI0MTIxNF5BMl5BanBnXkFtZTYwNTM0MzY2._V1_UX182_CR0,0,182,268_AL_.jpg",
                        "https://www.youtube.com/watch?v=o4gHCmTQDVI"))
    movies.append(Movie("Inception",
                        "A thief enters the dream world to surreptitiously implant an idea",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                        "https://www.youtube.com/watch?v=8hP9D6kZseM"))
    movies.append(Movie("Captain America: Civil War",
                        "The Avengers are torn apart by an internecine conflict",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjQ0MTgyNjAxMV5BMl5BanBnXkFtZTgwNjUzMDkyODE@._V1_UX182_CR0,0,182,268_AL_.jpg",
                        "https://www.youtube.com/watch?v=uVdV-lxRPFo"))
    movies.append(Movie("The Avengers",
                        "An unlikely team of superheroes assemble to save the world from an alien threat",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTk2NTI1MTU4N15BMl5BanBnXkFtZTcwODg0OTY0Nw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                        "https://www.youtube.com/watch?v=eOrNdBpGMv8"))
    movies.append(Movie("Avatar",
                        "A marine finds himself torn between his own race and the one he was sent to infiltrate",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY"))
    movies.append(Movie("The Sound of Music",
                        "A music-loving nun becomes governess to seven children",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BODIxNjhkYjEtYzUyMi00YTNjLWE1YjktNjAyY2I2MWNkNmNmL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR3,0,182,268_AL_.jpg",
                        "https://www.youtube.com/watch?v=9H4TTjDMTvA"))
    movies.append(Movie("It's a Wonderful Life",
                        "A struggling businessman struggles with whether to take his own life",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMzMzY5NDc4M15BMl5BanBnXkFtZTcwMzc4NjIxNw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                        "https://www.youtube.com/watch?v=nXsu5XArEUw"))
    movies.append(Movie("The Godfather",
                        "A young member of a crime family unwillingly becomes the godfather",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BZTRmNjQ1ZDYtNDgzMy00OGE0LWE4N2YtNTkzNWQ5ZDhlNGJmL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UY268_CR3,0,182,268_AL_.jpg",
                        "https://www.youtube.com/watch?v=sY1S34973zA"))

    open_movies_page(movies)

# Run the main function if the file is being run as main
if __name__ == '__main__':
    main()
