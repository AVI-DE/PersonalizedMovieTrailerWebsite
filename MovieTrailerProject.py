import fresh_tomatoes
import media

""" Defining the various instances of class movie """

seven_pounds = media.Movie("Seven Pounds",
                        "https://upload.wikimedia.org/wikipedia/en/2/2d/Seven_Pounds_poster.jpg",
                        "https://www.youtube.com/watch?v=MwrtEI-fcmM")

perfume = media.Movie("Perfume",
                    "https://upload.wikimedia.org/wikipedia/en/6/69/Perfume_poster.jpg",
                    "https://www.youtube.com/watch?v=_-qv0EnGhJU")

zero_dark_thirty = media.Movie("Zero Dark Thirty",
                            "https://upload.wikimedia.org/wikipedia/en/7/77/ZeroDarkThirty2012Poster.jpg",
                            "https://www.youtube.com/watch?v=YxC_JNz5Vbg")

snowden = media.Movie("Snowden",
                    "https://upload.wikimedia.org/wikipedia/en/c/ca/Snowden_film_poster.jpg",
                    "https://www.youtube.com/watch?v=QlSAiI3xMh4")

american_sniper = media.Movie("American Sniper",
                            "https://upload.wikimedia.org/wikipedia/en/1/10/American_Sniper_poster.jpg",
                            "https://www.youtube.com/watch?v=99k3u9ay1gs")

ex_machina = media.Movie("Ex Machina",
                        "https://upload.wikimedia.org/wikipedia/en/b/ba/Ex-machina-uk-poster.jpg",
                        "https://www.youtube.com/watch?v=EoQuVnKhxaM")

soul_surfer = media.Movie("Soul Surfer",
                        "https://upload.wikimedia.org/wikipedia/en/1/1d/Soul_Surfer_Poster.jpg",
                        "https://www.youtube.com/watch?v=_KlpD6dr7Qw")

august_rush = media.Movie("August Rush",
                        "https://upload.wikimedia.org/wikipedia/en/1/1b/August_rush_poster.jpg",
                        "https://www.youtube.com/watch?v=nRGYeyS1jzw")

forrest_gump = media.Movie("Forrest Gump",
                        "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
                        "https://www.youtube.com/watch?v=bLvqoHBptjg")

movies = [seven_pounds,perfume,zero_dark_thirty,snowden,american_sniper,ex_machina,soul_surfer,august_rush,forrest_gump]
fresh_tomatoes.open_movies_page(movies)
