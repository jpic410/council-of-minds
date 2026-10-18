from agent import Agent
from analysis import Analysis

def test_evaluate():
    skeptic = Agent(
        name="The Skeptic",
        role="Critical Thinker",
        personality="Analytical",
    )

    result = skeptic.evaluate("My Business Idea")

    assert isinstance(result, Analysis)
    assert "My Business Idea" in result.initial_analysis
    assert result.agent_name == "The Skeptic"