import sys


def morse():
    """\
small program that encodes a string as morse code
    output:
        the string encoded as morse code
    inputs:
        S a string
    """
    args = sys.argv
    if len(args) != 2:
        print("AssertionError: bad argument: need 1 arguments")
        return

    morse_code = {
        'A': '.-', 'B': '-...',
        'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.',
        'O': '---', 'P': '.--.', 'Q': '--.-',
        'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--',
        'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....',
        '7': '--...', '8': '---..', '9': '----.',
        '0': '-----', ' ': '/'}

    s = args[1]
    result = ""
    for char in s.upper():
        if result:
            result += " "
        try:
            result += morse_code[char]
        except KeyError:
            print("AssertionError: bad argument: invalid character")
            return

    print(result)


if __name__ == '__main__':
    morse()
