class PointsForPlace:
    @staticmethod
    def get_points_for_place(place: int):
        if place > 100:
            print('Баллы начисляются только первым 100 участникам')
            return 0
        elif place < 1:
            print('Спортсмен не может занять нулевое или отрицательное место')
            return 0
        else:
            return 101 - int(place)

class PointsForMeters:
    @staticmethod
    def get_points_for_meters(meters: int):
        if meters < 0:
            print('Количество метров не может быть отрицательным')
            return 0
        return meters * 0.5


class TotalPoints(PointsForPlace, PointsForMeters):
    def __init__(self):
        self.total = 0

    def get_total_points(self, meters: int, place: int):
        pts_place = self.get_points_for_place(place)
        pts_meters = self.get_points_for_meters(meters)
        self.total = pts_place + pts_meters
        return self.total


print(PointsForPlace.get_points_for_place(10))   
print(PointsForMeters.get_points_for_meters(10)) 

tp = TotalPoints()
print(tp.get_points_for_place(10))               
print(tp.get_points_for_meters(10))              
print(tp.get_total_points(10, 10))               
