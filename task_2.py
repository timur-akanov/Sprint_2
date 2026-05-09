class Movies:
    def __init__(self):
        self.movies =[]

    def add_movie(self, movie):
        self.movies.append(movie)

class Comedy(Movies):
    def add_movie(self, movie):
        self.movies.append(movie)
        return f"Комедии: {self.movies}"

class Drama(Movies):
    def add_movie(self, movie):
        self.movies.append(movie)
        return f"Драмы: {self.movies}"
    

c = Comedy()
print(c.add_movie('Большой куш'))

d = Drama()
print(d.add_movie('Оружейный барон'))
