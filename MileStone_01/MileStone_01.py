"""
- Enter 'a' to add a movie,
- Enter 'l' to see your movie
- Enter 'f' to find a movie
- Enter 'q' to quit

-- Add movies
-- See Movies
-- Find Movies
-- Stop running the program


Tasks:
[x]: Decide where to store movies
[]: What is the format of the movie
[x]: Show the user the main interface and get their input
[]: Allow users to add movies
[]: Show all their movies
[]: Find a movie
[x]: Stop running the program when they type 'q'
"""


movies = []    # ''' list to store movies '''

'''
movies = {
    'name' = ...(str),
    'director' = ...(str),
    'year' = ...(int)
    }
'''

def menu():
    user_input = input("Enter 'a' to add a movie, 'l' to see your list of movies, 'f' to find a movie. 'q' to quit")
    
    while user_input != 'q':
        if user_input == 'a':
           add_movie()
        elif user_input == 'l':
           show_movies()
        elif user_input == 'f':
           find_movie()
        else:
           print("Unknown Command, Please try again")
    ''' elif user_input =='q':
        print("Stopping Program....") '''

    user_input = input("Enter 'a' to add a movie, 'l' to see your list of movies, 'f' to find a movie. 'q' to quit")


def add_movie():
    name = input('Enater the movie name:  ')
    director = input("Enter the movie director's name: ")
    year = int((input('The year movie produced: '))

    movies.append({    # we did add the dictionary inside the append function. appending the dictionary to my list.
        'name': name,
        'director': director,
        'year': year
    })

"""
                    OR we can do it like this:
                                movie = {
                                    'name': name,
                                    'director': director,
                                    'year': year
                                    }
                                movie.append(movie)
"""

menu()

print(movies)

