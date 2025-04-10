
def get_book_text(path):
	return path.read()


with open("books/frankenstein.txt") as f:
    words = get_book_text(f)
    word_list = words.split()
    word_count = len(word_list)
    print(f"{word_count} words found in the document")