
def get_num_words(words):
    count = len(words)
    return count

def letter_count(words):
    text = words
    letters = {} 
    for char in text:
        if char.isalpha():
            lower_char = char.lower()
            letters[lower_char] = letters.get(lower_char,0) + 1
        else:
            letters[char] = letters.get(char,0) + 1
    return letters


