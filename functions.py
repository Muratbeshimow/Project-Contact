

import pickle

from classes import Contacts


def load_contacts():
    try:
        with open("contacts.pickle", 'rb') as f:
            contacts = pickle.load(f)
            return contacts
    except:
        with open("contacts.pickle", 'wb') as f:
            pickle.dump([], f)
            return []


def add_contact():
    contacts = load_contacts()
    name = input("name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    new_contact = Contacts(name=name, phone=phone, email=email)
    contacts.append(new_contact)
    print("Contact Added")
    save(contacts)


def save(list_save):
    with open("contacts.pickle", 'wb') as f:
        pickle.dump(list_save, f)


def view():
    contacts = load_contacts()
    print(contacts)


def update_contacts():
    contacts = load_contacts()
    user_input = input("Enter contact name to update:")
    print()
    for contact in contacts:
        if contact.name == user_input:
            contact.name = input("Enter the new name: ")
            contact.phone = input("Enter the new phohe: ")
            contact.email = input("Enter the new Email: ")
            print("contacts is updated")
            save(contacts)
            break
    else:
        print("contact not found")


def find_contact():
    contacts = load_contacts()
    user_input = input("Name to find: ")
    for contact in contacts:
        if contact.name == user_input:
            print(contact.name, contact.phone, contact.email)
            break
    else:
        print("Contact not found")


def remove_contact():
    contacts = load_contacts()
    user_input = input("Name to Remove: ")
    for contact in contacts:
        if contact.name == user_input:
            contacts.remove(contact)
            save(contacts)
            print("Contacts", contact.name, "Removed")
            break
    else:
        print("contact not found")
