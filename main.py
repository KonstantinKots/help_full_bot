from datetime import datetime

'''
Додаток для збереження нотаток

This is my note, that I am talking on my laptop
- Created on 09.02.2026 19:45 ❤

[("This is my note, that I am talking on my laptop", "09.02.2026 19:45")]
[("09.02.2026 19:45", "This is my note, that I am talking on my laptop")]

{"text": "This is my note, that I am talking on my laptop", "creation_date": "09.02.2026 19:45"}

1) створити словник нотаток та додати в нього інформацію
2) написати функцію яка буде виводити нотатки
3) написати функцію яка буде виводити всі нотатки
4) написати цикл який буде отримувати інформацію від користувача та реагувати на неї
'''

note_list = [] #[{"text": "This is my note, that I am talking on my laptop", "creation_date": "09.02.2026 19:45"}]
note_file = "notes.txt"

# Hello note; 09.02.2026 19:45

welcom_banner = '''
 █████   █████          ████                                  █████               █████   
▒▒███   ▒▒███          ▒▒███                                 ▒▒███               ▒▒███    
 ▒███    ▒███   ██████  ▒███  ████████   ██████  ████████     ▒███████   ██████  ███████  
 ▒███████████  ███▒▒███ ▒███ ▒▒███▒▒███ ███▒▒███▒▒███▒▒███    ▒███▒▒███ ███▒▒███▒▒▒███▒   
 ▒███▒▒▒▒▒███ ▒███████  ▒███  ▒███ ▒███▒███████  ▒███ ▒▒▒     ▒███ ▒███▒███ ▒███  ▒███    
 ▒███    ▒███ ▒███▒▒▒   ▒███  ▒███ ▒███▒███▒▒▒   ▒███         ▒███ ▒███▒███ ▒███  ▒███ ███
 █████   █████▒▒██████  █████ ▒███████ ▒▒██████  █████        ████████ ▒▒██████   ▒▒█████ 
▒▒▒▒▒   ▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒▒▒▒  ▒███▒▒▒   ▒▒▒▒▒▒  ▒▒▒▒▒        ▒▒▒▒▒▒▒▒   ▒▒▒▒▒▒     ▒▒▒▒▒  
                              ▒███                                                        
                              █████                                                       
                             ▒▒▒▒▒                                                        
'''

commands ='''
1) exit - to exit the application
2) add_note - to add a new note
3) print_note [i] - to print note number i
4) print_all - to print all notes
5) help - to print this menu
'''

def add_new_note(note_text) -> bool:
    note_creation_date = datetime.today()
    note_list.append({"text": note_text, "creation_date": note_creation_date})
    return True

def print_note(index: int):
    note = note_list[index]
    #09.02.2026 19:45 dd:mm:yyyy hh:mm
    formatted_creation_date = note["creation_date"].strftime("%d.%m.%Y %H:%M")
    print(f'"{note["text"]}"\n- Created on {formatted_creation_date}\n')

def print_all_note():
    for note_index in range(len(note_list)):
        print_note(note_index)

def save_notes():
    with open(note_file, 'w', encoding='utf-8') as file:
        for note in note_list:
            file.write(f"{note["text"]};{note["creation_date"]}\n") #\n для запису нової нотатки з нової строки

def read_notes() -> list[dict]:
    note_list = []
    with open(note_file) as file:
        for line in file:
            text, date = line.strip().split(';')
            creation_date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")
            note_list.append({"text": text, "creation_date": creation_date})
    return note_list

def init():
    global note_list
    note_list = read_notes() #при запуску програми файл зчитує старі нотатки
    print(welcom_banner)
    print("\nHello and welcome to our app!\n")
    print(commands)
    print()

def main():
    while (True):
        command, *args = input("Please enter your command (enter exit to stop): ").strip().split(" ")
        if command == "exit":
            save_notes() # після введення exit викликаємо зберігання нотаток
            print("Goodbye!")
            break
        elif command == "add_note":
            text = input("Please enter note text: ")
            if add_new_note(text):
                print("\nNote added successfully!\n")
            else:
                print("\nError while adding note!\n")
        elif command == "help":
            print(commands)
        elif command == "print_note":
            index = int(args[0]) - 1
            if index < 0 or index >= len(note_list):
                print("Please enter a valid note number")
                continue
            print_note(index)
        elif command == "print_all": #дописати функцію
            print()

init()
main()

# text = input("Please enter note text: ")
# add_new_note(text)
# add_new_note(text)
# add_new_note(text)
# add_new_note(text)
# add_new_note(text)

# print_all_note()
#Ctrl C
