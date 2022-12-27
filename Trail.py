from PrimordialLocation import PrimordialLocation

class Trail:

    # This is the real location class. It functions as the Node in the linked list.
    class Location:
        def __init__(self, name: str, position: int):
            self.name = name
            self.position = position
            self.next = None
            self.prev = None
        

    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None



    def add_locations(self, loc_list: list[PrimordialLocation]) -> None:
        # Convert from a list of strings to a list of locations
        location_list = []
        for prime_location in loc_list:
            location_list.append(self.Location(prime_location.name, prime_location.position))

        for i_loc in range(len(location_list)):
            if i_loc == 0:
                # assign head
                self.head = location_list[i_loc]
                self.head.next = location_list[i_loc+1]
            elif (i_loc != len(location_list)-1) and (i_loc != 0):
                # This is the middle of the linked list.
                # Hook up the current node to the next and previous nodes.
                location_list[i_loc].prev = location_list[i_loc-1]
                location_list[i_loc].next = location_list[i_loc+1]
            elif i_loc == len(location_list):
                # We are at the end.
                # assign tail and connect to previous node.
                self.tail = location_list[i_loc]
                self.tail.prev = location_list[i_loc-1]
        # make the current pointer point at something
        self.current = self.head
    
    def display_locations(self):
        current_node = self.head
        while current_node != None:
            print (f"{current_node.name}, {current_node.position}")
            current_node = current_node.next

    def update_current_location(self):
        if self.current != None:
            self.current = self.current.next

    def match_position_to_location(self, position: int) -> str:
        current_node = self.head
        while current_node != None:
            if current_node.position == position:
                return current_node.name
            current_node = current_node.next
        # if we make it this far, we must not have found any matches
        return "nowhere specific"