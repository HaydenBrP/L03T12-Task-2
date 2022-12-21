# This program takes in a users movies description and then selects the
# most similar movie from a file of movie options.

# Import modules. Load language models.
import spacy

nlp = spacy.load('en_core_web_md')
                 
# Create class variable to store data from file.
class Movie:
    
    def __init__ (self, title, score):
        self.title = title
        self.score = score

# Create a function to display the class variable.
def __repr__(self):
        return f'{self.title}.'

# Requested a description from the user. 
input_desc = input("Please type in a detailed description of your favourite movie? ")

# Parse the input through the nlp language model.
pars_input_desc = nlp(input_desc)

print("\n")

# Open the movie.txt file and read the information to file.
# Sort the information, parse each option through the nlp model for comparson.
# Loop through the list and save the items to the class variable array.
with open ('movies.txt', 'r') as movie_f :
    movie_f_desc = movie_f.readlines()

    movie_list = []
    
    for desc in movie_f_desc :
        par_f_desc = nlp(desc)

        movie_list.append(Movie(desc[:7], par_f_desc.similarity(pars_input_desc)))

# Sort the array, decending by the similarity.
sorted_movies = sorted(movie_list, key=lambda x: x.score, reverse=True)

# isolate the first option from the sorted arra.
for items in sorted_movies:
    next_movie = __repr__(items)
    break

#Print out the result.
print(f'Based on your description the best movie for you to watch next is: {next_movie}')
