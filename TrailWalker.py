""" 
    Class representing a person on the trail.
 """

class TrailWalker:
    def __init__(self, name: str):
        self.name = name
        self.conditions = []
    
    def __repr__(self):
        return f"{self.name:30}{self.list_conditions()}"
    
    def list_conditions(self):
        return_string = ""
        for i_con in range(len(self.conditions)):
            return_string += f"{self.conditions[i_con]}"
            if i_con != len(self.conditions):
                return_string += ", "
        return return_string