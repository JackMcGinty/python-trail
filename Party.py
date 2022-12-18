import random
class Party:
    def __init__(self, trail):
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
        if self.distance_traveled + distance > self.trail.next_stop.position:
            distance = self.trail.next_stop.position - self.distance_traveled
        print(f"Traveled {distance} miles.")
        if self.distance_traveled == self.trail.next_stop.position:
            print(f"Arrived at {self.trail.next_stop.name}")
            
        self.distance_traveled += distance

    