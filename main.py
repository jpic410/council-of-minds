from agent import Agent


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

    



if __name__ == "__main__":
    main()