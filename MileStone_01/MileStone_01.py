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
[]: Decide where to store movies
[]: What is the format of the movie
[]: Show the user the main interface and get their input
[]: Allow users to add movies
[]: Show all their movies
[]: Find a movie
[]: Stop running the program when they type 'q'
"""



def menu():
    user_input = input("Enter 'a' to add a movie, 'l' to see your list of movies, 'f' to find a movie. 'q' to quit")

    While user_input != 'q':
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

menu()