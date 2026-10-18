from agent import Agent
from analysis import Analysis


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

    my_idea = "My Business Idea"

    result = skeptic.evaluate(my_idea)

    print(result.initial_analysis)
    print(result.questions)
    

    



if __name__ == "__main__":
    main()