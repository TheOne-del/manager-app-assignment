from workout import Workout

class LongRun(Workout):
    def __init__(self, name: str, duration_minutes: int, calories_burned: float, distance_miles: float):
        super().__init__(name, duration_minutes, calories_burned)
        self.distance_miles = distance_miles  # Extra detail: distance in miles

    def display(self):
        print(f"  • [Long Run]  {self.name}: {self.duration_minutes} mins | {self.calories_burned} cal | Distance: {self.distance_miles} miles")