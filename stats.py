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

def second(letters):
    dict_list =[]
    for letter in letters:
        dict_list.append({'character':letter, 'count':letters[letter]})
    return dict_list

def sort_on(dict_list):
    return dict_list['count']

def main():
    words = "This is The Test STRIng"
    print(sorted(second(letter_count(words)), reverse=True, key=sort_on))

if __name__ == "__main__":
    main()
