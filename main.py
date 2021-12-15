from airport import Airport
from door_agent import DoorAgent

class Main:
    def __init__(self, env, passenger):
        self.airport = Airport(env, passenger)
        self.door_agent = DoorAgent(self.airport)
        self.door_agent.start()

    def run(self):
        self.door_agent.start()


if __name__ == '__main__':
    import simpy
    env = simpy.Environment()
    # passenger object
    passenger = {
        'name': 'John Doe',
        'destination': 'BKK',
        'flight_number': 'AA123',
        'seat_number': 'A1',
        'passport': '123456789',
        'ticket': '123456789'
    }
    main = Main(env, passenger)
    main.run()