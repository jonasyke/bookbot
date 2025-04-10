from stats import get_num_words
def get_book_text(path):
	return path.read()


with open("books/frankenstein.txt") as f:
    words = get_book_text(f)
    word_list = words.split()
    count = get_num_words(word_list)
    print(f"{count} words found in the document")