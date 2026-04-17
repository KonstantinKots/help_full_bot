from datetime import datetime
from id_generator import id_generator
from colorama import Fore, Back, Style
from printer_fuction import print_error, print_success, input_colored
from classes import NoteUser

'''
Додаток для збереження нотаток

This is my note, that I am talking on my laptop
- Created on 09.02.2026 19:45 ❤😊

[("This is my note, that I am talking on my laptop", "09.02.2026 19:45")]
[("09.02.2026 19:45", "This is my note, that I am talking on my laptop")]

{"text": "This is my note, that I am talking on my laptop", "creation_date": "09.02.2026 19:45"}

1) створити словник нотаток та додати в нього інформацію
2) написати функцію яка буде виводити нотатки
3) написати функцію яка буде виводити всі нотатки
4) написати цикл який буде отримувати інформацію від користувача та реагувати на неї
5) пофіксити проблему глобальної змінної
6) пофіксити проблему відсутності аргументів у print_note
'''

note_list = [] #[{"text": "This is my note, that I am talking on my laptop", "creation_date": "09.02.2026 19:45", "id": 1}]
note_file = "notes.txt"
note_id_generator = id_generator()
users_list = []

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

def add_new_note(note_text, curren_user: NoteUser) -> bool:
    note_creation_date = datetime.today()
    next_id = note_id_generator()
    note_list.append({"text": note_text, "creation_date": note_creation_date, "id": next_id})
    curren_user.notes_id.append(next_id)
    return True

def print_note(index: int, current_user: NoteUser):
    note = note_list[index]
    if note["id"] not in current_user.notes_id:
        print_error("User can not access this note")
        return
    formatted_creation_date = note["creation_date"].strftime("%d.%m.%Y %H:%M")
    print(f'{note["id"]}: "{note["text"]}"\n- Created on {formatted_creation_date}\n')

def print_all_note(current_user: NoteUser):
    for note_index in range(len(note_list)): 
       print_note(note_index, current_user)

# def find_top_note_id(notes: list[dict]) -> int:
#     max_id = 0
#     for note in notes:
#         note_id = note["id"]
#         if note_id > max_id:
#             max_id = note_id
#     return max_id

# def find_top_note_id_funcional(notes: list[dict]) -> int:
#     note_ids =[0]
#     for note in notes:
#         note_ids.append(note["id"])
#     return max(note_ids)

def find_top_note_id_funcional(notes: list[dict]) -> int:
    return max([note["id"] for note in notes] + [0])


def save_notes():
    with open(note_file, 'w', encoding='utf-8') as file:
        for note in note_list:
            file.write(f"{note["id"]};{note['text']};{note['creation_date']}\n")

def read_notes() -> list[dict]:
    note_list = []
    with open(note_file) as file:
        for line in file:
            if ";" not in line:
                continue
            id, text, date = line.strip().split(';')
            creation_date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")
            note_list.append({"id": int(id), "text": text, "creation_date": creation_date})
    return note_list

def init_note_app():
    global note_list
    note_list = read_notes()

    max_note = find_top_note_id_funcional(note_list)

    global note_id_generator
    note_id_generator = id_generator(max_note)

    print(welcom_banner)
    print("\nHello and welcome to our app!\n")
    print(commands)
    print()

def find_user_dy_login(login: str) -> NoteUser| None:
    note_user = None
    for user in users_list:
        if user.login == login:
            note_user = user
    return note_user

def get_user() -> NoteUser:
    user_login = input_colored("Please enter your username:")
    found_user = find_user_dy_login(user_login)
    if not found_user:
        print_error("User not found")
        found_user = NoteUser(user_login)
        users_list.append(found_user)
        print_success("New User added")
    return found_user

def main():
    current_user = get_user()
    while (True):
        command, *args = input_colored("Please enter your command (enter exit to stop): ").strip().split()
        if command == "exit":
            save_notes()
            print("Goodbye!")
            break
        elif command == "add_note":
            text = input_colored("Please enter note text: ")
            if add_new_note(text, current_user):
                print_success("\nNote added successfully!\n")
            else:
                print_error("\nError while adding note!\n")
        elif command == "help":
            print(commands)
        elif command == "print_note":
            if len(args) < 1:
                print_error("Please enter a note number")
                continue
            index = int(args[0]) - 1
            if index < 0 or index >= len(note_list):
                print_error("Please enter a valid note number")
                continue
            else:
                print_note(index, current_user)
        elif command == "print_all":
            if not note_list:
                print_error("Notes file is empty")
                continue
            print_all_note(current_user)
        

init_note_app()
main()

