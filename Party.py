from Trail import Trail
import random
class Party:
    def __init__(self, trail: Trail):
        self.distance_traveled = 0
        self.members = []
        self.trail = trail
        
    def display_party(self):
        for member in self.members:
            print(member)
        pass

    def __repr__(self):
        pass

    def travel(self):
        """ Randomly determine how many miles the gang traveled today. """
        distance = random.randint(10, 20)
        # We'll alter this according to various party conditions.
        if self.distance_traveled + distance > self.trail.next_stop.position:
            distance = self.trail.next_stop.position - self.distance_traveled
        print(f"Traveled {distance} miles.")
        if self.distance_traveled == self.trail.next_stop.position:
            print(f"Arrived at {self.trail.next_stop.name}")
            self.trail.update_current_stop()
            
        self.distance_traveled += distance

    """ Run the party on our trail until we either (1) reach the end or (2) die. """
    def run(self):
        # When the trail's current stop is none, we'll be at the end of the trail.
        while self.trail.current != None:
            # determine how far we traveled.
            print("Time for another day's travel.")
            self.travel()
            # trigger an event?


        
