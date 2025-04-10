
def get_book_text(path):
	return path.read()


with open("books/frankenstein.txt") as f:
    print(get_book_text(f))