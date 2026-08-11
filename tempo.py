from workout import Workout

class TempoRun(Workout):
    def __init__(self, name: str, duration_minutes: int, calories_burned: float, target_pace: str):
        super().__init__(name, duration_minutes, calories_burned)
        self.target_pace = target_pace  # Extra detail: e.g., "7:15 min/mi"

    def display(self):
        print(f"  • [Tempo Run] {self.name}: {self.duration_minutes} mins | {self.calories_burned} cal | Target Pace: {self.target_pace}")