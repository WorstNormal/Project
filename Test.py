
command = input("What are you doing next? ")
match command.split():
    case ["quit"]:  # введено одно слово "quit"
        print("Goodbye!")
    case ["look"]:  # введено одно слово "look"
        print("current_room.describe()")
    case ["get", obj]:  # введено два слова - "get" и какое-то другое, которое будет записано в переменную obj
        print("character.get(obj, current_room)")
    case ["go", direction]:
        print("current_room = current_room.neighbor(direction)")
    case ["drop", *objects]:  # введено слово "drop" и еще несколько слов, которые будут записаны в переменную objects
        for obj in objects:
            character.drop(obj, current_room)
    case _:  # Аналогично default в других языках
        print(f"Sorry, I couldn't understand {command!r}")