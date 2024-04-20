import JulioLexer as JL

if __name__ == "__main__":
    Lexer = JL.JulioLexer()

    # open the sample file
    with open("JulioSays.j", "r") as file:
        # read each line of the file
        for line_number, line in enumerate(file, 1):
            print(f"Reading line {line_number}: {line}")  # print the line being read
            # tokenize the line
            tokens = Lexer.tokenize(line, line_number)
            print(tokens)
            print()