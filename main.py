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

        command_parts = command.split(" ")
        command_parts[0] = command_parts[0].lower()  # Convert command to lowercase

        if command_parts[0] == "add":
            name = command_parts[1]
            record = Record(name)
            phones = command_parts[2:]
            for phone in phones:
                record.add_phone(phone)
            address_book.add_record(record)
            print(f"Contact {name} added successfully")

        elif command_parts[0] == "delete":
            name = command_parts[1]
            address_book.delete_record(name)
            print(f"Contact {name} deleted successfully")

        elif command_parts[0] == "edit":
            name = command_parts[1]
            phones = command_parts[2:]
            if name in address_book.data:
                record = address_book.data[name]
                record.phones = []
                for phone in phones:
                    record.add_phone(phone)
                print(f"Contact {name} edited successfully")
            else:
                print(f"No contact found with name {name}")

        elif command_parts[0] == "search":
            if len(command_parts) == 2:
                name = command_parts[1]
                results = address_book.search_records(name=name)
                for record in results:
                    print(f"Name: {record.name.value}")
                    for phone in record.phones:
                        print(f"Phone: {phone.value}")
                    print()
            else:
                print("Invalid command. Please provide a name to search.")

        elif command_parts[0] in ["exit", "quit"]:
            print("Good bye!")
            break

        else:
            print("Invalid command. Please try again.")


if __name__== "__main__":
    main()
