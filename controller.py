import view as v
import model as m

def main():
    while True:
        n = v.main_menu()
        match (n):
            case "1":
                v.menu_viewing_contacts(m.phone_book)
            case "2":
                phone_book_list = v.menu_create_contact()
                m.create_contact(phone_book_list)
            case "3":
                surname = v.menu_find_contact()
                contact = m.find_contact(surname)
                v.menu_view_find_contact(contact)
            case "4":
                m.import_html()
            case "5":
                m.import_csv()
            case "6":
                m.import_json()
            case "7":
                m.export_html()
            case "8":
                m.export_csv()
            case "9":
                m.export_json()
            case "q":
                break

