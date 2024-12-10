import string
def shorten(word: str)-> str:
    """_ A program that converts a str to a str without vowels whether in uppercase or lowercase_

    Args:
        word (str): _Word to convert_
        
    Returns:
        (str): __Word without vowels
        
    Example:
        >>> shorten("HELLO")
            "HLL"
        >>> shorten("hello")
            "hll"
    """
    
    
    twttr_output = [consonant for consonant in word if consonant not in ['a','e','i','o','u','A','E','I','O','U'] ]
    return "".join(twttr_output)
    
def main()-> None:
    word: str = input("Word: ").strip()
    short_word: str = shorten(word) 
    print(f"Word wuthout vowels: {short_word}")

if __name__ == "__main__":
    main()
