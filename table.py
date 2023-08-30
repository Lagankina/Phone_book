phone_book = {}
PATH = "phone_book_Adel.txt"

def open_file(book: dict):
    with open(PATH, 'r' , encoding='UTF-8') as file:
        data = file.readlines()
    for i, contact in enumerate(data,1):
        contact = contact.strip().split(";")
        book[i] = contact
        
def save_file(book: dict):
    all_contacts = []
    for contact in book.values():
        all_contacts.append(";".join(contact))
    with open(PATH, 'w' , encoding='UTF-8') as file:   
        file.write('\n'.join(all_contacts))
        
def show_contacts(book: dict, message: str):
    print("\n" + "=" * 67)
    if book:
        for i, contact in book.items():
            print(f"{i:>3}. {contact[0]:<20} {contact[1]:<20} {contact[2]:<20}")
    else:
        print(message)
    print("=" * 67 + "\n")
    
def add_new_contact(book: dict, new: list):
    cur_id = max(book.keys())  + 1
    book[cur_id] = new 
    
def find_contact(book: dict, search: str):
    result = {}
    for i, contact in book.items():
        for field in contact:
            if search.lower() in field.lower():
                result[i] = contact
                break
    return result
def func_search(book: dict, cid: int):
    name, phone, comment = book.get(cid)
    ch = []
    for item in ["Введите новое имя (или оставьте пустым, чтоюы не изменять): ",
                 "Введите телефон (или оставьте пустым, чтоюы не изменять): ",
                 "Введите коммент (или оставьте пустым, чтоюы не изменять): "]:
        ch.append(input(item))
    book[cid] = [ch[0] if ch[0] else name,ch[1] if ch[1] else phone, ch[2] if ch[2] else comment]
    return ch[0] if ch[0] else name

def menu():
    menu_points = ["Открыть файл", "Сохранить файл", "Посмотреть все контакты", "Добавить контакт", "Найти контакт", "Изменить контакт", "Удалить контакт", "Выход"]
    print ("Главное меню")
    [print(f'\t{i}. {item}') for i , item in enumerate(menu_points,1)]
    choice = int(input("Выберите пункт меню: "))
    return choice