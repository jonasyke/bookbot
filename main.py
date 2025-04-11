def main():
    from stats import get_num_words, list_sorter
    def get_book_text(path):
        return path.read()


    with open("books/frankenstein.txt") as f:
        words = get_book_text(f)
        word_list = words.split()
        count = get_num_words(word_list)

    print("============ BOOKBOT ============ \nAnalyzing book found at books/frankenstein.txt... \n----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    new_list = list_sorter(words)
    for l in new_list:
        print(f"{l['character']}: {l['count']}")
    print("============= END ===============")
main()