import random
import string

class Passenger:
    def __init__(self, name, ticket, passport):
        self.name = name
        self.ticket = ticket
        self.passport = passport

    def generate_random_passengers(self, count):
        for i in range(count):
            yield self.generate_random_passenger()

    def generate_random_passenger(self):
        name = self.generate_random_name()
        ticket = self.generate_random_ticket()
        passport = self.generate_random_passport()
        return Passenger(name, ticket, passport)

    def generate_random_name(self):
        return ''.join(random.choice(string.ascii_letters) for i in range(10))

    def generate_random_ticket(self):
        return ''.join(random.choice(string.digits) for i in range(6))

    def generate_random_passport(self):
        return ''.join(random.choice(string.digits) for i in range(9))

    def __str__(self):
        return '{} {} {}'.format(self.name, self.ticket, self.passport)

    def __repr__(self):
        return '{} {} {}'.format(self.name, self.ticket, self.passport)

    def __eq__(self, other):
        return self.name == other.name and self.ticket == other.ticket and self.passport == other.passport
        