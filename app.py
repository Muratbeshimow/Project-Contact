from functions import add_contact, find_contact, remove_contact, view, update_contacts
while True:
    option = input("""
[A]dd
[v]iew
[f]ind                       
[r]emove 
[u]pdate
                                                    
                    Choise: """)

    if option == 'a':
        add_contact()
    if option == 'v':
        view()
    if option == 'u':
        update_contacts()
    if option == 'f':
        find_contact()
    if option == 'r':
        remove_contact()
    if option == 'q':
        break
