def words_count(text):
    print(len(text.split()))
    return len(text.split())

def letters_count(text):
    text = text.lower()
    letters = {}
    for word in text:
        for letter in word:
            if not letter in letters:
                letters[letter] = 1
                continue
            letters[letter] += 1
    return letters

def dict_of_chars_to_list(dict):
    letters = []
    for letter in dict:
        if letter.isalpha():
            letters.append({
                "name": letter,
                "num": dict[letter]
            })
    return letters

def sort_on(dict):
    return dict["num"]

def main():
    with open("books/frankenstein.txt") as f:
        content = f.read()
        words_count(content)
        letters = dict_of_chars_to_list(letters_count(content))
        letters.sort(reverse=True, key=sort_on)
        for letter in letters:
            print(f"The '{letter}' character was found {letter["num"]} times")
        

main()
