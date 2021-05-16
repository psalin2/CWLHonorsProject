import matplotlib.pyplot as plt

from imdb import IMDb

ia = IMDb()

# IMDb IDs for the Top Indian films from 2000-2009
movie_IDs = ['0284137', '1187043', '0248126', '1166100', '0441048', '0234000', '1024943', '0254481', '1182937',
             '0456144', '0213890', '0238936', '0488798', '0871510', '0169102', '0807758', '1146325', '0420332',
             '0439662', '1017456', '0451833', '0461936', '0405508', '0986264', '0449994', '1275863', '0473367',
             '0248185', '1252596', '0995031', '0347473', '0449999', '1084972', '0806088', '0300028', '0307873',
             '0419058', '0448206', '1092005', '0151150', '0418362', '0499375', '0805184', '0422091', '0250690',
             '0294662', '1185420']

# Dictionary with IMDb IDs for each of the films corresponding to the adjusted gross in Indian rupee
movie_adjusted_gross = {'0284137': 2865500000, '1187043': 2695000000, '0248126': 1727000000, '1166100': 1705000000,
                        '0441048': 1467800000, '0234000': 1387600000, '1024943': 1332100000, '0254481': 1300900000,
                        '1182937': 1287000000, '0456144': 1274000000, '0213890': 1247800000, '0238936': 1224100000,
                        '0488798': 1121000000, '0871510': 1181400000, '0169102': 1054800000, '0807758': 1034000000,
                        '1146325': 1033700000, '0420332': 1009200000, '0439662': 1000800000, '1017456': 970900000,
                        '0451833': 952200000, '0461936': 941400000, '0405508': 936900000, '0986264': 935800000,
                        '0449994': 932500000, '1275863': 910100000, '0473367': 907500000, '0248185': 890000000,
                        '1252596': 847000000, '0995031': 840500000, '0347473': 837500000, '0449999': 828800000,
                        '1084972': 828200000, '0806088': 820900000, '0300028': 812500000, '0307873': 798600000,
                        '0419058': 797500000, '0448206': 775200000, '1092005': 768400000, '0151150': 766200000,
                        '0418362': 762500000, '0499375': 746100000, '0805184': 744600000, '0422091': 742000000,
                        '0250690': 741400000, '0294662': 729000000, '1185420': 724700000}


def find_common_cast():
    """
    This method parses through the cast of all the movies ands adds them to a dictionary that keeps track of how many
    times the specific actor/actress has acted in the list of films.
    :return: A dictionary with the name of the cast member as the key and the number of appearances as the value
    """
    common_cast = {}
    for movie in movie_IDs:
        for actor in ia.get_movie(movie)['cast']:
            if actor['name'] in common_cast.keys():
                common_cast[actor['name']] += 1
            else:
                common_cast[actor['name']] = 1
    return common_cast


def find_common_directors():
    """
    This method parses through the directors of all the movies ands adds them to a dictionary that keeps track of how
    many films they have directed.
    :return: A dictionary with the name of the director as the key and the number of movies as the value
    """
    common_directors = {}
    for movie in movie_IDs:
        for director in ia.get_movie(movie)['directors']:
            if director['name'] in common_directors.keys():
                common_directors[director['name']] += 1
            else:
                common_directors[director['name']] = 1
    return common_directors


def plot_common_cast_graph():
    """
    This method plots a bar graph with the most common actors/actresses of the decade for the popular films
    and the number of films they acted in them.
    :return: Bar graph of common cast members as the y-axis and number of acting performances.
    """
    common_cast = find_common_cast()
    actors = []
    num_of_films_acted_in = []

    for actor in common_cast.keys():
        if common_cast[actor] > 4:
            actors.append(actor)
            num_of_films_acted_in.append(common_cast[actor])

    plt.barh(actors, num_of_films_acted_in)
    plt.xlabel('# of film performances')
    plt.ylabel('Actor/Actress')
    plt.title('Common Cast in the Top Films of 2000-2009')
    plt.tight_layout()
    plt.show()


def plot_common_directors_graph():
    """
    This method plots a bar graph with the most common directors of the decade for the popular films and the number
    of films they directed.
    :return: Bar graph of common directors as the y-axis and number of films as x-axis.
    """
    common_directors = find_common_directors()
    directors = []
    num_of_movies = []

    for director in common_directors.keys():
        if common_directors[director] > 1:
            directors.append(director)
            num_of_movies.append(common_directors[director])

    plt.barh(directors, num_of_movies)

    plt.xlabel('# of movies')
    plt.ylabel('Director')
    plt.title('Common Directors in the Top Films of 2000-2009')
    plt.tight_layout()
    plt.show()


def get_budget_as_number(unedited_budget):
    separated = unedited_budget.split(' ')
    if 'AUD' in separated[0] or 'INR' in separated[0]:
        edited_budget = separated[0].replace(',', '')[3:-1]
    else:
        edited_budget = separated[0].replace(',', '')[1:-1]
    return int(edited_budget)
def plot_budget_and_adjusted_gross_scatter_plot():
    """
    This method plots the budget of each film in relation to the adjusted gross.
    :return: A scatter plot of the budget vs adjusted gross of each film.
    """
    adjusted_gross = []
    budget = []
    for movieId in movie_IDs:
        if 'box office' in ia.get_movie(movieId).keys():
            if 'Budget' in ia.get_movie(movieId)['box office'].keys():
                money_in_billions = movie_adjusted_gross[movieId] / 1000000000
                adjusted_gross.append(money_in_billions)
                budget.append(get_budget_as_number(ia.get_movie(movieId)['box office']['Budget']))
                print((get_budget_as_number(ia.get_movie(movieId)['box office']['Budget']) / 1000000))

    plt.scatter(budget, adjusted_gross)
    plt.title('Budget of Films vs Adjusted Gross')
    plt.xlabel("Budget")
    plt.ylabel('Adjusted Gross (INR in billions)')
    plt.show()


# Plotting of graphs
# plot_common_directors_graph()
# plot_common_cast_graph()
plot_budget_and_adjusted_gross_scatter_plot()
