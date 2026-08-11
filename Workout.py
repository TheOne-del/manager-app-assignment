class Workout:
    def __init__(self, name: str, duration_minutes: int, calories_burned: float):
        self.name = name
        self.duration_minutes = duration_minutes
        self.calories_burned = calories_burned
        
        # Check for bad numbers right away!
        self.check_calories()

    def check_calories(self):
        """Rejects negative numbers for calories."""
        if self.calories_burned < 0:
            print(f"  ⚠️ Oops! '{self.name}' had negative calories ({self.calories_burned}). Resetting to 0.")
            self.calories_burned = 0.0

    def display(self):
        print(f"  • {self.name}: {self.duration_minutes} mins | {self.calories_burned} cal")