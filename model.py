import csv
import json

phone_book = {}
id = 0

def create_contact(phone_book_list):
    global phone_book
    global id
    phone_book[id] = phone_book_list
    id += 1
    return phone_book

def find_contact(surname):
    for contact in phone_book.values():
        if surname == contact[0]:
            return contact

def import_html():
    with open("phone_book.html", "w", encoding='utf-8') as h:
        h.writelines(f"<html lang='ru'>"
                     f"<head>"
                     f"<meta charset='utf-8'>"
                     f"<title>Телефонная книга</title>"
                     f"</head>"
                     f"<body>"
                     f"<h2>Телефонная книга</h2>"
                     f"</body>"
                     f"</html>")
        for contact in phone_book.values():
            h.writelines(f"<html lang='ru'>"
                         f"<meta charset='utf-8'>"
                         f"<body>"
                         f"<p>{contact[0]} {contact[1]}: {contact[2]}</p>"
                         f"</body>"
                         f"</html>")

def export_html():
    global phone_book
    global id
    with open("phone_book.html", "r", encoding='utf-8') as h:
        s = h.readline()
        # print(s)
        # print(type(s))
    s = s.replace(f"<html lang='ru'>"
                     f"<head>"
                     f"<meta charset='utf-8'>"
                     f"<title>Телефонная книга</title>"
                     f"</head>"
                     f"<body>"
                     f"<h2>Телефонная книга</h2>"
                     f"</body>"
                     f"</html>", "")
    s = s.replace(f"<html lang='ru'>"
                         f"<meta charset='utf-8'>"
                         f"<body>"
                         f"<p>", "")
    s =  s.replace("</p>"
                         f"</body>"
                         f"</html>", " ")
    s = s.replace(":", "")
    s_list = s.split(" ")
    for i in range(0, 3):
        phone_book[id] = [s_list[3*i+0], s_list[3*i+1], s_list[3*i+2]]
        id += 1
    return phone_book

def import_csv():
    with open("phone_book.csv", "w", encoding='utf-8') as c:
        for contact in phone_book.values():
            wr = csv.writer(c, delimiter=';', lineterminator="\r")
            wr.writerow(contact)

def export_csv():
    global id
    global phone_book
    with open("phone_book.csv", "r", encoding='utf-8') as c:
        wr = csv.reader(c, delimiter=';', lineterminator="\r")
        for i in wr:
            phone_book[id] = i
            id += 1
    return phone_book

def import_json():
    with open('phone_book.json', 'w', encoding='utf-8') as f:
        json.dump(phone_book, f, ensure_ascii=False)

def export_json():
    global phone_book
    with open('phone_book.json', 'r', encoding='utf-8') as f:
        phone_book = json.load(f)
    return phone_book

