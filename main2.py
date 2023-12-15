from collections import UserDict
import re

class Field:
    def __init__(self, value):
        self.value = value

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not re.fullmatch(r"\d{10}", value):
            raise ValueError("Phone number must have 10 digits.")
        super().__init__(value)

class Record:
    def __init__(self, name, phones=[]):
        self.name = Name(name)
        self.phones = [Phone(phone) for phone in phones]

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                break

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        return f"Name: {self.name.value}, Phones: {', '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

# Приклад використання
book = AddressBook()

# Створення та додавання записів
john_record = Record("John", ["1234567890", "5555555555"])
book.add_record(john_record)
jane_record = Record("Jane", ["9876543210"])
book.add_record(jane_record)

# Виведення записів
for record in book.data.values():
    print(record)

# Редагування номеру
john = book.find("John")
if john:
    john.edit_phone("1234567890", "1112223333")
    print(john)

# Пошук телефону
found_phone = john.find_phone("5555555555")
if found_phone:
    print(f"Found phone for John: {found_phone.value}")

# Видалення запису
book.delete("Jane")
