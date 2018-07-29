# coding: utf-8

def print_words(new_words_list):
    words_list = new_words_list
    print(words_list)
    word_input = str(input("Please enter one one to add to your list, or press Enter to finalise your list:  "))
    if word_input == "":
        print("Here is your sorted word list:  ")
        print(sorted(words_list))
    else:
        words_list.append(word_input)
        print_words(words_list)

print_words([])
