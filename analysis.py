from dataclasses import dataclass

@dataclass
class Analysis:
    agent_name: str
    initial_analysis: str
    strenghts: list[str]
    weakpoints: list[str]
    questions: list[str]