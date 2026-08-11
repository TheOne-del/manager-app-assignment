from tempo import TempoRun
from longruns import LongRun
from trail import Trail


def main():
    # Warm greeting
    print("--------------------------------------------------")
    print("   🌲 Hello runner! Welcome to your Trail Tracker.")
    print("--------------------------------------------------")

    # Ask the user for the trail name to create the Boss object
    trail_name = input("\nWhat is the name of the trail you are running today? ")
    trail_boss = Trail(trail_name)

    print(f"\nAwesome! We are tracking runs for: {trail_name}")

    # Interactive Loop
    while True:
        print("\n" + "=" * 40)
        print("   --- TRAIL MENU ---")
        print("   1. Log a Tempo Run")
        print("   2. Log a Long Run")
        print("   3. Show Trail Summary & Total Calories")
        print("   4. Exit")
        print("=" * 40)

        choice = input("Please select an option (1-4): ").strip()

        if choice == "1":
            print("\n📝 --- Logging a Tempo Run ---")
            name = input("Enter run name (e.g., Hill Sprints): ")
            duration = int(input("Enter duration (minutes): "))
            calories = float(input("Enter calories burned: "))
            pace = input("Enter target pace (e.g., 7:15 min/mi): ")

            # Create Kind 1 object
            run = TempoRun(name, duration, calories, pace)
            trail_boss.add_workout(run)

        elif choice == "2":
            print("\n📝 --- Logging a Long Run ---")
            name = input("Enter run name (e.g., Ridge Loop): ")
            duration = int(input("Enter duration (minutes): "))
            calories = float(input("Enter calories burned: "))
            distance = float(input("Enter distance (miles): "))

            # Create Kind 2 object
            run = LongRun(name, duration, calories, distance)
            trail_boss.add_workout(run)

        elif choice == "3":
            # Display the Boss summary
            trail_boss.show_summary()

        elif choice == "4":
            # Polite goodbye and break out of the loop
            print(f"\n🎉 Great job on the trails today! Keep up the hard work! 👋\n")
            break

        else:
            print("❌ Invalid option. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()