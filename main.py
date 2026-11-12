
import json
import os

FILE_NAME = "notes.json"


def load_notes():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_notes(notes):
    with open(FILE_NAME, "w") as file:
        json.dump(notes, file, indent=4)


def add_note(notes):
    title = input("Enter note title: ")
    content = input("Enter note content: ")

    notes.append({"title": title, "content": content})
    save_notes(notes)
    print("Note added successfully!")


def view_notes(notes):
    if not notes:
        print("No notes available.")
        return

    for i, note in enumerate(notes, 1):
        print(f"\n{i}. {note['title']}")
        print(note["content"])


def search_notes(notes):
    keyword = input("Enter search keyword: ").lower()

    found = False

    for note in notes:
        if keyword in note["title"].lower() or keyword in note["content"].lower():
            print(f"\nTitle: {note['title']}")
            print(f"Content: {note['content']}")
            found = True

    if not found:
        print("No matching notes found.")


def edit_note(notes):
    view_notes(notes)

    try:
        number = int(input("Enter note number to edit: "))

        if 1 <= number <= len(notes):
            notes[number - 1]["title"] = input("New title: ")
            notes[number - 1]["content"] = input("New content: ")
            save_notes(notes)
            print("Note updated successfully!")
        else:
            print("Invalid note number.")

    except ValueError:
        print("Please enter a valid number.")


def delete_note(notes):
    view_notes(notes)

    try:
        number = int(input("Enter note number to delete: "))

        if 1 <= number <= len(notes):
            notes.pop(number - 1)
            save_notes(notes)
            print("Note deleted successfully!")
        else:
            print("Invalid note number.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    notes = load_notes()

    while True:
        print("\n===== CAMPUSNOTES =====")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Search Notes")
        print("4. Edit Note")
        print("5. Delete Note")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_note(notes)
        elif choice == "2":
            view_notes(notes)
        elif choice == "3":
            search_notes(notes)
        elif choice == "4":
            edit_note(notes)
        elif choice == "5":
            delete_note(notes)
        elif choice == "6":
            print("Thank you for using CampusNotes!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
