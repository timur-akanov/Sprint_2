class Movies:
    movies = []  # атрибут класса — общий для всех экземпляров

    @classmethod
    def add_movie(cls, movie):
        cls.movies.append(movie)


class Comedy(Movies):
    @classmethod
    def add_movie(cls, movie):
        super().add_movie(movie)
        return f"Комедии: {cls.movies}"


class Drama(Movies):
    @classmethod
    def add_movie(cls, movie):
        super().add_movie(movie)
        return f"Драмы: {cls.movies}"


print(Comedy.add_movie('Большой куш'))
print(Drama.add_movie('Оружейный барон'))
