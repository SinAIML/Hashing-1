"""Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.
Example 1:

Input: pattern = "abba", s = "dog cat cat dog"

Output: true"""

#Time complexity: O(n) where n is the length of the pattern or the number of words in s
#Space complexity: O(n) for the hash map and set
#Approach: We can use a hash map to store the mapping of characters in the pattern to words in s, and a set to keep track of the words that have already been mapped. We iterate through the pattern and the list of words simultaneously, checking for consistency in the mapping. If we find any inconsistency, we return False. If we successfully process the entire pattern and list of words, we return True.
#Leetcode: Yes


def wordPattern(pattern, s):

    slist = s.split(" ")
    print(slist)

    if len(pattern) != len(slist):
            return False
    pmap = {}
    smap = set()

    for i in range(len(pattern)):
        char = pattern[i]
        word = slist[i]
        
        if char not in pmap:
            # If the char is new, but the word is already used by another char
            if word in smap:
                return False
            # Create the new mapping
            pmap[char] = word
            smap.add(word)
        else:
            # If the char is already mapped, it must match the current word
            if pmap[char] != word:
                return False