import json
from pathlib import Path

path = Path("phones.json")

if path.exists():
    f = open("phones.json", "r")
    phone_list = json.load(f)
    f.close()
else:
    phone_list = {}

commands = ["new_contact", "show_contacts"]
while True:
    command = input(f"Pick and option: {commands} ")
    while command not in commands:
        print("Unknown command, try again")
        command = input(f"Pick and option: {commands} ")
    if command == "new_contact":
        name = input("Wprowadz swoje imie i nazwisko: ")
        phone_number = input("Wprowadz numer telefonu: ")
        phone_list[name] = phone_number
    elif command == "show_contacts":
        print(phone_list)
    #else:
     #   print("Unknown command")
    answer = input("Do you want to continue Y/N: ")
    while answer.lower() not in ["y", "n"]:
        print("Choose Y or N only")
        answer = input("Do you want to continue Y/N: ")

    if answer.lower() == "n":
        f = open("phones.json", "w")
        json.dump(phone_list, f)
        f.close()
        break

