# Airport Door Controller Agent
# Simulates a door controller agent

# import libraries
import sys
import time
import os


class DoorAgent:
    def __init__(self, passenger):
        self.door_state = 'closed'
        self.door_id = 'A'
        self.passenger = passenger

    def get_door_state(self):
        return self.door_state

    def get_door_id(self):
        return self.door_id

    def set_door_state(self, door_state):
        self.door_state = door_state

    def set_door_id(self, door_id):
        self.door_id = door_id

    def open_door(self):
        self.door_state = 'open'

    def close_door(self):
        self.door_state = 'closed'

    def toggle_door(self):
        if self.door_state == 'open':
            self.door_state = 'closed'
        else:
            self.door_state = 'open'

    def check_for_person(self, passenger):
        if passenger == self.passenger:
            return True
        else:
            return False

    def start(self):
        print('Door Agent is running...')
        while True:
            time.sleep(1)

    def join(self):
        pass




