from agent import Agent
from analysis import Analysis

class Council:
    def __init__ (self, agents: list[Agent]):
        self.agents = agents

    def evaluate(self, idea:str) -> list[Analysis]:
        evaluations = []
        for agent in self.agents:
            analysis = agent.evaluate(idea)
            evaluations.append(analysis)
        return evaluations

    