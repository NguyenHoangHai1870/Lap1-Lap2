from RegrexTokenizer import RegrexTokenizer
from SimpleTokenizer import SimpleTokenizer

if __name__ == "__main__":
    sentences= [
        "Hello, world! This is a test.",
        "NLP is fascinating... isn't it?",
        "Let's see how it handles 123 numbers and punctuation!"
    ]

    regrex = RegrexTokenizer()
    simple = SimpleTokenizer()

    for sentence in sentences:
        print(f"{sentence}",end="\n")
        print(f"regrextokenizer output: {regrex.tokenize(sentence)}", end="\n")
        print(f"simpletokenizer output: {simple.tokenize(sentence)}", end="\n")
        print("-" * 50)