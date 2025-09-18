from SimpleTokenizer import SimpleTokenizer
if __name__ == "__main__":
    tokenizer = SimpleTokenizer()
    text = "Hello , world!"
    token = tokenizer.tokenize(text)
    print(token)