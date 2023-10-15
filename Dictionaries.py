phone_list={}

while True:
    command = input("Pick and option: new_contact , show_contacts ")
    if command == "new_contact":
        name = input("Wprowadz swoje imie i nazwisko: ")
        phone_number = input("Wprowadz numer telefonu: ")
        phone_list[name] = phone_number
    elif command == "show_contacts":
        print(phone_list)
    #else:
     #   print("Unknown command")
    command = input("Do you want to continue Y/N ")
    if command == "N":
        break

