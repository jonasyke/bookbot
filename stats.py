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
    return letters

def second(letters):
    dict_list =[]
    for letter in letters:
        dict_list.append({'character':letter, 'count':letters[letter]})
    return dict_list

def sort_on(dict_list):
    return dict_list['count']

def list_sorter(words):
    return sorted(second(letter_count(words)), reverse=True, key=sort_on)

def main():
    words = "THis IS the TEST StrING"
    task = sorted(second(letter_count(words)), reverse=True, key=sort_on)
    for t in task:
        if t['character'].isalpha():
            print(f"{t['character']}: {t['count']}")

if __name__ == "__main__":
    main()
