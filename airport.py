import simpy
import random
import statistics


class Airport(object):
    def __init__(self, env, passenger):
        self.env = env
        self.passenger = passenger
        self.ticket = "123456789"
        self.passport = "123456789"
        self.name = "John Doe"
        self.queue = simpy.Resource(env, capacity=1)

    def check_ticket(self, passenger):
        if passenger.ticket == self.ticket:
            print("{} checked in at {}".format(passenger.name, self.name))
            return True
        else:
            return False
        
    def check_passport(self, passenger):
        if passenger.passport == self.passport:
            print("{} checked in at {}".format(passenger.name, self.name))
            return True
        else:
            return False

    def check_in(self, passenger):
        yield self.env.timeout(random.randint(1, 10))
        if self.check_ticket(passenger) or self.check_passport(passenger):
            print("{} checked in at {}".format(passenger.name, self.name))
            return True
        else:
            print("{} was denied boarding at {}".format(passenger.name, self.name))
            return False

    def check_out(self, passenger):
        yield self.env.timeout(random.randint(1, 10))
        print("{} checked out at {}".format(passenger.name, self.name))

    def board(self, passenger):
        with self.queue.request() as req:
            yield req
            yield self.env.process(self.check_in(passenger))
            yield self.env.process(self.check_out(passenger))

    def allow_through_door(self, passenger):
        # if check_in(passenger) == True:, open the door, else deny boarding
        yield self.env.timeout(random.randint(1, 10))
        if self.check_in(passenger):
            print("{} allowed through the door at {}".format(passenger.name, self.name))
            return True
        else:
            print("{} was denied boarding at {}".format(passenger.name, self.name))
            return False