# anagram problem
# two strings are anagrams if they are made of same characters with same frequencies-just in different order.
# s1=danger, s2= garden are anagrams

# hash table used to record frequency of each character in each string.
# hash table maps unqinue keys to values.
from collections import Counter


def check_anagram(s1, s2):
    if len(s1) != len(s2):
        # check if both strings have same length-if not they are not anagrams.
        return False

    # two hash tables to record frequencies of characters in each string.
    freq_string_1 = {}
    freq_string_2 = {}

    for ch in s1:
        if ch in freq_string_1:  # if character already present in hash table, increment freq. by 1
            freq_string_1[ch] += 1
        else:
            freq_string_1[ch] = 1  # else set freq. to 1

    for ch in s2:
        if ch in freq_string_2:
            freq_string_2[ch] += 1
        else:
            freq_string_2[ch] = 1

    for key in freq_string_1:
        if key not in freq_string_2 or freq_string_1[key] != freq_string_2[key]:
            # if character of S1 doesn't exist in S2 or they Don't appear same number of times.
            return False
    return True


def check_anagram_python(s1, s2):
    # python version of same code
    if len(s1) != len(s2): 
        return False
    return Counter(s1) == Counter(s2) #in-built library


print(check_anagram('salesmen', 'nameless'))
print(check_anagram('garden', 'danger'))

print(check_anagram_python('salesmen', 'nameless'))
print(check_anagram_python('garden', 'danger'))
