from analysis import Analysis

class Agent:
    def __init__(self, name, role, personality):
        self.name = name
        self.role = role
        self.personality = personality

    def introduction(self):
        return f"I am {self.name}, a {self.role}.\n"

    def evaluate(self, idea: str) -> Analysis:
        return Analysis(
            agent_name=self.name,
            initial_analysis= f"Initial analysis of {idea} from {self.name}!", #placeholder
            strenghts=["strenghts"],
            weakpoints=["weakness"],
            questions=[f"follow up questions for {idea}"],
        )