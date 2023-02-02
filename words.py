# For a list of words, print out each word on a separate line, but in all uppercase. How can you change a word to uppercase? Ask Python for help on what you can do with strings!

# Turn that into a function, print_upper_words. Test it out. (Don’t forget to add a docstring to your function!)

# Change that function so that it only prints words that start with the letter ‘e’ (either upper or lowercase).

# Make your function more general: you should be able to pass in a set of letters, and it only prints words that start with one of those letters.

def print_upper_words(list):
    """Print each word in all caps.

        >>> print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])
        HELLO
        HEY
        GOODBYE
        YO
        YES
    """
    for word in list:
        print(word.upper())



def print_upper_words(list):
    """Print each word if starts with H or h.
    
        >>> print_upper_words2(["hello", "hey", "goodbye", "yo", "yes"])
        HELLO
        HEY
    """
    for word in list:
        if word[0] == 'h' or word[0] == 'H':
            print(word.upper())


def print_upper_words3(list, must_start_with):
    """Print each word in all caps if it starts with one of given

        >>> print_upper_words3(["hello", "hey", "goodbye", "yo", "yes"],
        ...                   must_start_with=["h", "g"])
        HELLO
        HEY
        GOODBYE
    """
    for word in list:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break