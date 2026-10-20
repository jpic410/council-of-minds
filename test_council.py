from council import Council
from agent import Agent
from analysis import Analysis

def test_if_council_returns_one_analysis_per_agent():
    skeptic = Agent("Skeptic", "Critic", "Analytical")
    investor = Agent("Investor", "Finance", "Pragmatic")
    visionary = Agent("Visionary", "Innovator", "Forward-thinkink")

    council = Council([skeptic, investor, visionary])

    idee = "Eine Lern-App"

    evaluations = council.evaluate(idee)
    
    assert len(evaluations) == 3
    
    names = []
    for analysis in evaluations:
        names.append(analysis.agent_name)
    
    assert names == ["Skeptic", "Investor", "Visionary"]
    
    for analysis in evaluations:
        assert isinstance(analysis, Analysis)
        assert idee in analysis.initial_analysis
