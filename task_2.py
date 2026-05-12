class Movies:
    def __init__(self):
        # Инициализируем пустой список для хранения фильмов
        self.movies = []

    def add_movie(self, movie):
        # Добавляем фильм в конец списка
        self.movies.append(movie)


class Comedy(Movies):
    def add_movie(self, movie):
        # Вызываем метод родителя для добавления фильма в список
        super().add_movie(movie)
        # Возвращаем отформатированную строку для комедий
        return f"Комедии: {self.movies}"


class Drama(Movies):
    def add_movie(self, movie):
        # Вызываем метод родителя для добавления фильма в список
        super().add_movie(movie)
        # Возвращаем отформатированную строку для драм
        return f"Драмы: {self.movies}"


# Создание объекта комедии и добавление фильма
comedy_instance = Comedy()
result_comedy = comedy_instance.add_movie('Большой куш')
print(result_comedy)

# Создание объекта драмы и добавление фильма
drama_instance = Drama()
result_drama = drama_instance.add_movie('Оружейный барон')
print(result_drama)
