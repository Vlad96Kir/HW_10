from collections import UserDict


class Field:
    def __init__(self, value=None):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                break


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def delete_record(self, name):
        del self.data[name]

    def edit_record(self, name, new_record):
        self.data[name] = new_record

    def search_records(self, **kwargs):
        results = []
        for record in self.data.values():
            match = True
            for key, value in kwargs.items():
                if key == 'name':
                    if record.name.value != value:
                        match = False
                        break
                elif key == 'phone':
                    if not any(phone.value == value for phone in record.phones):
                        match = False
                        break
            if match:
                results.append(record)
        return results


def main():
    address_book = AddressBook()

    while True:
        command = input("> ")

        if command.startswith("add"):
            _, name, phone = command.split(" ")
            record = Record(name)
            record.add_phone(phone)
            address_book.add_record(record)
            print(f"Contact {name} with phone {phone} added successfully")
        elif command.startswith("delete"):
            _, name = command.split(" ")
            if name in address_book.data:
                address_book.delete_record(name)
                print(f"Contact {name} deleted successfully")
            else:
                print(f"No contact found with the name {name}")
        elif command.startswith("edit"):
            _, name, phone = command.split(" ")
            if name in address_book.data:
                record = address_book.data[name]
                record.add_phone(phone)
                address_book.edit_record(name, record)
                print(f"Phone number for contact {name} changed to {phone}")
            else:
                print(f"No contact found with the name {name}")
        elif command.startswith("search"):
            _, field, value = command.split(" ")
            if field == "name":
                results = address_book.search_records(name=value)
                if results:
                    print("Search results:")
                    for record in results:
                        print(f"{record.name.value}: {', '.join(phone.value for phone in record.phones)}")
                else:
                    print("No contacts found")
            elif field == "phone":
                results = address_book.search_records(phone=value)
                if results:
                    print("Search results:")
                    for record in results:
                        print(f"{record.name.value}: {', '.join(phone.value for phone in record.phones)}")
                else:
                    print("No contacts found")
        elif command == "exit":
            break
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
