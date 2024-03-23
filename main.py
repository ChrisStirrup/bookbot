"""The Bookbot program"""

def main():
    """Generates the book report"""
    history = "/home/chrisstirrup/workspace/github.com/ChrisStirrup/bookbot/books/History.txt"
    shelly =  "/home/chrisstirrup/workspace/github.com/ChrisStirrup/bookbot/books/frankenstein.txt"
    book_path = input('Please enter a path to your .txt document: ')
    if book_path in ('shelly', ''):
        book_path = shelly
    if book_path == 'history':
        book_path = history
    text = get_book_text(book_path)
    print("Book Report")
    print(f"There are {word_count(text)} words found in this document")
    for thing in sort_letter_frequency(text):
        print(f"The '{thing['letter']}' letter was found '{thing['frequency']}' times")
    print("Thus endeth the report.")

def get_book_text(path):
    """Returns all the text from the given path"""
    with open(path, encoding="utf-8") as f:
        return f.read()

def word_count(document):
    """Returns the count of words in the given string"""
    return len(document.split())

def letter_frequency(document):
    """Returns a set containing the count of each word in the given string"""
    letter_count = {}
    for d in document.lower():
        if d in letter_count:
            letter_count[d] += 1
        else:
            letter_count[d] = 1
    return letter_count

def sort_on(d):
    """Sorting function on the key 'frequency'"""
    return d["frequency"]

def sort_letter_frequency(document):
    """Returns a sorted list containing the frequency of each letter in the given string"""
    letter_count = letter_frequency(document)
    only_alphabets = {}
    sorted_list = []
    for item in letter_count.items():
        if item[0].isalpha():
            only_alphabets[item[0]] = item[1]
    for letter, frequency in only_alphabets.items():
        sorted_list.append({'letter': letter, "frequency": frequency})
        sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()
