from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return self.value


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, phone_number):
        if self.is_valid_number(phone_number):
            super().__init__(phone_number)
        else:
            raise ValueError

    def is_valid_number(self, phone_number):
        if (phone_number.isdigit() and len(phone_number) == 10):
            return True
        else:
            return False


class Record:
    # реалізація класу
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number):
        for phone in self.phones:
            if phone_number == phone.value:
                self.phones.remove(phone)
                return phone

    def edit_phone(self, phone_number, phone_number_new):
        for phone in self.phones:
            if phone.value == phone_number:
                self.remove_phone(phone_number)
                self.add_phone(phone_number_new)
                return phone_number, phone_number_new
        raise ValueError

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone_number == phone.value:
                print(self.name, ': ', phone_number)
                return phone

    def __str__(self):
        phones = '; '.join(p.value for p in self.phones)
        return f"Contact name: {self.name}, phones: {phones}"


class AddressBook(UserDict):
    # реалізація класу

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        return self.data.pop(name, None)
        # if name in self.data:
        #     del self.data[name]

    def __str__(self) -> str:
        records = 'Book records:\n'
        for n, k in self.data.items():
            records += f"Contact name: {n}, phones: {
                '; '.join(p.value for p in k.phones)}\n"
        return records


if __name__ == '__main__':

    # Створення нової адресної книги

    book = AddressBook()
    john_record = Record("John")
    john_record.add_phone("1234567890")
    # john_record.add_phone("17234567890")
    john_record.add_phone("5555555555")
    print(john_record.name)
    print(john_record.phones)
    # john_record.remove_phone('0987654321')

    # Додавання запису John до адресної книги
    book.add_record(john_record)
    print(book.data['John'])

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: <{found_phone}>")  # Виведення: 5555555555

    # Видалення запису Jane
    # book.delete("Jane")
    print(book)
