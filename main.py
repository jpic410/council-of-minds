from agent import Agent
from analysis import Analysis
from council import Council


def main():
    print("Welcome to Council of Minds!")
    print("Where ideas meet critical thinking.\n")

    skeptic = Agent(
        "The Skeptic",
        "Critical Thinker",
        "Analytical and questioning"
    )
    print(skeptic.introduction())

    investor = Agent(
        "The Investor",
        "Financial Analyst",
        "Pragmatic and profit-oriented",
    )
    print(investor.introduction())

    idea = "My fantastic Business idea!"

    council = Council([skeptic, investor])
    eval = council.evaluate(idea)
    for analysis in eval:
        print(analysis.agent_name)
        print(analysis.initial_analysis)


    

    



if __name__ == "__main__":
    main()