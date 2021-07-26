# Task: Write a program that takes in a word list and outputs a list of all the words that are anagrams of another
# word in the list.
word_list = ["percussion", "supersonic", "car", "tree", "boy", "girl", "arc"]

# Solution 1: using 2 for loops
anagram_list1 = []
for word_1 in word_list:
    for word_2 in word_list:
        if word_1 != word_2 and (sorted(word_1) == sorted(word_2)):
            anagram_list1.append(word_1)

print(f"Solution 1:\n {anagram_list1}")


# Solution 2: using Dictionaries
def freq(word):
    freq_dict = {}
    for char in word:
        freq_dict[char] = freq_dict.get(char, 0) + 1
    return freq_dict


anagram_list2 = []
for word_1 in word_list:
    for word_2 in word_list:
        if word_1 != word_2 and (freq(word_1) == freq(word_2)):
            anagram_list2.append(word_1)
print(f"Solution 2 with Dictionaries:\n {anagram_list2}")
