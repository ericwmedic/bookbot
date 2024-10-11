def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        char_count = count_characters(file_contents)
        sorted_char_count = sort_characters_by_count(char_count)
        print_report(path_to_file, word_count, sorted_char_count)

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def sort_characters_by_count(char_count):
    char_list = [{"character": char, "count": count} for char, count in char_count.items()]
    char_list.sort(key=lambda x: x["count"], reverse=True)
    return char_list

def print_report(path_to_file, word_count, sorted_char_count):
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{word_count} words found in the document\n")
    for item in sorted_char_count:
        print(f"The '{item['character']}' character was found {item['count']} times")
    print("--- End report ---")

if __name__ == "__main__":
    main()