from workout import Workout

class Trail:
    def __init__(self, trail_name: str):
        self.trail_name = trail_name
        self.workout_list = []

    def add_workout(self, workout: Workout):
        self.workout_list.append(workout)
        print(f"  ✅ Success! Added '{workout.name}' to the trail log.")

    def show_summary(self):
        print("\n" + "=" * 55)
        print(f"  🌲 SUMMARY FOR TRAIL: {self.trail_name.upper()} 🌲")
        print("=" * 55)
        
        if len(self.workout_list) == 0:
            print("  No runs logged yet for this trail!")
        else:
            print("  Logged runs:")
            for item in self.workout_list:
                item.display()
                
        # Total up the calories
        total_calories = 0
        for item in self.workout_list:
            total_calories += item.calories_burned
            
        print("-" * 55)
        print(f"  🔥 Great progress! Total Calories Burned: {total_calories:.1f} cal")
        print("=" * 55)