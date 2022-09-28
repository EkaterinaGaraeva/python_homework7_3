def main_menu():
    print("Телефонная книга")
    n = input("Введите:\n"
              "1 - для просмотра контактов\n"
              "2 - для создания нового контакта\n"
              "3 - поиск контакта\n"
              "4 - импорт в html\n"
              "5 - импорт в csv\n"
              "6 - импорт в json\n"
              "7 - экспорт из html\n"
              "8 - экспорт из csv\n"
              "9 - экспорт из json\n"
              "q - выход\n"
              "-> ")
    return n

def menu_viewing_contacts(phone_book):
    for contact in phone_book.values():
        print(f"{contact[0]} {contact[1]}: {contact[2]}")

def menu_create_contact():
    print("Введите данные")
    phone_book_list = []
    phone_book_list.append(input("Фамилия: "))
    phone_book_list.append(input("Имя: "))
    phone_book_list.append(input("Телефонный номер: "))
    return phone_book_list

def menu_find_contact():
    surname = input("Введите фамилию: ")
    return surname

def menu_view_find_contact(contact):
    print(f"{contact[0]} {contact[1]}: {contact[2]}")

