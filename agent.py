
class Agent:
    def __init__(self, name, role, personality):
        self.name = name
        self.role = role
        self.personality = personality

    def introduction(self):
        return f"I am {self.name}, a {self.role}.\n"