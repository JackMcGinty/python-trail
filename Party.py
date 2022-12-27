from Trail import Trail
from TrailWalker import TrailWalker
import random
class Party:
    def __init__(self, trail: Trail, names: list[str]):
        self.distance_traveled = 0
        self.members = []
        self.populate_members(names)
        self.trail = trail
        # put us on the first stop.
        self.trail.update_current_location()
        
    def populate_members(self, names: list[str]):
        for name in names:
            self.members.append(TrailWalker(name))
        
        
    def display_party(self):
        print ("Party status: ")
        # TODO morale or something
        for member in self.members:
            print(member)
        pass

    def __repr__(self):
        pass

    def travel(self):
        """ Randomly determine how many miles the gang traveled today. """
        distance = random.randint(10, 20)
        # mess with distance as conditions allow
        print (f"Starting from {self.trail.match_position_to_location(self.distance_traveled)}")
        # We'll alter this according to various party conditions.
        if self.distance_traveled + distance > self.trail.current.position:
            distance = self.trail.current.position - self.distance_traveled
        self.distance_traveled += distance
        print(f"Traveled {distance} miles.")
        if self.distance_traveled == self.trail.current.position:
            print(f"Arrived at {self.trail.current.name}")
            self.trail.update_current_location()
            

    """ Run the party on our trail until we either (1) reach the end or (2) die. """
    def run(self):
        # When the trail's current stop is none, we'll be at the end of the trail.
        while self.trail.current != None:
            # determine how far we traveled.
            print("\nTime for another day's travel.")
            self.travel()
            
            # trigger an event? (random)
            # activate event from the location (if applicable)
            # display the party's status
            self.display_party()