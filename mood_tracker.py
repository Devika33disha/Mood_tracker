class MoodEntry:
    def __init__(self, mood, note, date):
        self.mood = mood
        self.note = note
        self.date = date

    def display(self):
        return f"{self.date} | {self.mood} | {self.note}"


class MoodTracker:
    def __init__(self):
        self.entries = []

    def add_entry(self, entry):
        self.entries.append(entry)

    def view_entries(self):
        if not self.entries:
            print("\nNo mood entries recorded yet.")
            return

        print("\n----- Mood History -----")
        for i, entry in enumerate(self.entries, start=1):
            print(f"{i}. {entry.display()}")

    def mood_summary(self):
        if not self.entries:
            print("\nNo mood entries to summarize.")
            return

        summary = {}
        for entry in self.entries:
            summary[entry.mood] = summary.get(entry.mood, 0) + 1

        print("\n----- Mood Summary -----")
        for mood, count in summary.items():
            print(f"{mood}: {count}")

    def most_common_mood(self):
        if not self.entries:
            print("\nNo mood entries available.")
            return

        summary = {}
        for entry in self.entries:
            summary[entry.mood] = summary.get(entry.mood, 0) + 1

        max_mood = max(summary, key=summary.get)
        print(f"\nMost frequent mood: {max_mood} ({summary[max_mood]} times)")


def get_valid_mood():
    moods = ["Happy", "Sad", "Angry", "Calm", "Excited", "Tired", "Anxious", "Neutral"]
    print("\nAvailable moods:", ", ".join(moods))

    while True:
        mood = input("Enter your mood: ").strip().title()
        if mood in moods:
            return mood
        print("Invalid mood! Please choose from the given list.")


def get_valid_text(prompt, allow_empty=False):
    while True:
        value = input(prompt).strip()
        if allow_empty or value:
            return value
        print("Invalid input! This field cannot be empty.")


def get_valid_date():
    while True:
        date = input("Enter date (DD-MM-YYYY): ").strip()
        parts = date.split("-")

        if len(parts) == 3 and all(part.isdigit() for part in parts):
            day, month, year = map(int, parts)
            if 1 <= day <= 31 and 1 <= month <= 12 and year > 0:
                return date

        print("Invalid date! Please enter in DD-MM-YYYY format.")


tracker = MoodTracker()

while True:
    print("\n=== Mood Tracker Menu ===")
    print("1. Add Mood Entry")
    print("2. View Mood History")
    print("3. Show Mood Summary")
    print("4. Show Most Frequent Mood")
    print("5. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        mood = get_valid_mood()
        note = get_valid_text("Enter a short note (optional): ", allow_empty=True)
        date = get_valid_date()

        entry = MoodEntry(mood, note if note else "No note", date)
        tracker.add_entry(entry)
        print("Mood entry added successfully!")

    elif choice == "2":
        tracker.view_entries()

    elif choice == "3":
        tracker.mood_summary()

    elif choice == "4":
        tracker.most_common_mood()

    elif choice == "5":
        print("Exiting Mood Tracker. Take care!")
        break

    else:
        print("Invalid choice! Please select from 1 to 5.")