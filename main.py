import sys 

import stats 

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    stats.print_report(book_path)
