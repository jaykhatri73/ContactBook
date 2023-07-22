
class ContactBook:
    def __init__(self):
        self.contacts = {}

    # to add contact
    def add_contact(self, name, phone_number):
        self.contacts[name] = phone_number
        print("Contact added successfully!")

    # to remove contact
    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print("Contact removed successfully!")
        else:
            print("Contact not found.")

    # to search contact
    def search_contact(self, name):
        if name in self.contacts:
            print(f"Name: {name}\tPhone Number: {self.contacts[name]}")
        else:
            print("Contact not found.")

    # to display saved contacts
    def display_contacts(self):
        print("Contact List:")
        for name, phone_number in self.contacts.items():
            print(f"Name: {name}\tPhone Number: {phone_number}")
            print(". . . End of Contact book. . .")

# main function


def main():
    contact_book = ContactBook()
    # greeting and option to choose from
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Search Contact")
        print("4. Display Contacts")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        # to add contact
        if choice == '1':
            name = input("Enter the name: ")
            phone_number = input("Enter the phone number: ")
            contact_book.add_contact(name, phone_number)

        # to remove contact
        elif choice == '2':
            name = input("Enter the name: ")
            contact_book.remove_contact(name)

        # to search contact
        elif choice == '3':
            name = input("Enter the name: ")
            contact_book.search_contact(name)

        # to display saved contacts
        elif choice == '4':
            contact_book.display_contacts()

        # to close the program
        elif choice == '5':
            print("Exiting Contact Book...")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


main()
