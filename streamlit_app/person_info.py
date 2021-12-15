from datetime import date, timedelta

class Address:
    def __init__(self, street, number, neighboorhood, complement, zip_code) -> None:
        self.street = street
        self.number = number
        self.neighboorhood = neighboorhood
        self.complement = complement
        self.zip_code = zip_code

class Person:
    def __init__(self, name: str, last_name: str, gender: str, birthdate: date, address: Address) -> None:
        self.name = name
        self.last_name = last_name
        self.gender = gender
        self.birthdate = birthdate
        self.address = address
        