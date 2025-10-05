from typing import TypedDict 
class counts_dict(TypedDict):
    char: str
    num: int 

def get_book_text(book_path: str)-> str:
    with open(book_path, 'r') as book:
        return book.read()

def get_word_count(book_text: str)-> int:
    words = book_text.split()
    return len(words)

def get_char_stats(book_text: str)-> dict[str, int]:
    char_stats = dict()
    for ch in book_text:
        c = ch.lower()
        char_stats[c] = char_stats.get(c, 0) + 1
    return char_stats


def sort_stats(char_stats: dict[str, int])-> list[counts_dict]:
    list_of_counts = [{"char": k, "num": v} for k, v in char_stats.items()]
    list_of_counts.sort(reverse = True, key = lambda x: x["num"])
    return list_of_counts

def print_report(book_path: str)-> None:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    book_text = get_book_text(book_path)

    word_count = get_word_count(book_text)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    char_stats   = get_char_stats(book_text)
    sorted_stats = sort_stats(char_stats)
    print("--------- Character Count -------")
    for count in sorted_stats:
        ch  = count["char"]
        num = count["num"]
        if (ch.isalpha()):
            print(f"{ch}: {num}")

    print("============= END ===============")
