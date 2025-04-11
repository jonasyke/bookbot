def main():
    import sys
    from stats import get_num_words, list_sorter
    def get_book_text(path):
        return path.read()
    try:
        if len(sys.argv) != 2:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)
        book = sys.argv[1]
        with open(f"{book}") as f:
            words = get_book_text(f)
            word_list = words.split()
            count = get_num_words(word_list)

        print(f"============ BOOKBOT ============ \nAnalyzing book found at books/{book}... \n----------- Word Count ----------")
        print(f"Found {count} total words")
        print("--------- Character Count -------")
        new_list = list_sorter(words)
        for l in new_list:
            print(f"{l['character']}: {l['count']}")
        print("============= END ===============")
    except Exception as e:
        print("invalid path")
main()