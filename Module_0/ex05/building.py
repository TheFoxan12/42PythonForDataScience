import sys


def main():
    """takes a single string argument and displays the sums of its \
upper-case characters, lower-case characters, punctuation \
characters, digits and spaces"""
    args = sys.argv
    if len(args) > 2:
        print("AssertionError: more than one argument is provided")

    if len(args) < 2:
        string = input("What is the text to count ?\n>>")
    else:
        string: str = args[1]

    punctuation = list(".,;:?!()[]{}“”‘’'\"…-_/`")
    nb_up = 0
    nb_low = 0
    nb_punc = 0
    nb_digits = 0
    nb_spaces = 0
    for char in string:
        nb_up += char.isupper()
        nb_low += char.islower()
        nb_digits += char.isdigit()
        nb_spaces += char.isspace()
        nb_punc += (char in punctuation)

    print(f"The text contains {len(string)} characters:\n"
          f"{nb_up} upper letters\n"
          f"{nb_low} low letters\n"
          f"{nb_punc} punctuation marks\n"
          f"{nb_spaces} spaces\n"
          f"{nb_digits} digits")


if __name__ == '__main__':
    main()
