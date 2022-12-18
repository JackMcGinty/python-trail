from Event import Event

class Location:
    def __init__(self, name: str, specific_event: Event, position: int):
        self.name = name
        self.event = specific_event
        self.position = position
    
