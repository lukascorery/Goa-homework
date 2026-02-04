"""12) დაწერე ფუნქცია, რომელიც იღებს სიტყვების სიას და აბრუნებს სიის ყველაზე გრძელ სიტყვას. გამოიყენე ციკლი და 'len()' შედარებისთვის"""
def find_longest_word(word_list):
    longest_word = ""
    for word in word_list:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word
