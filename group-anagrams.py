"""Given an array of strings strs, group the 

together. You can return the answer in any order.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]"""
#strs = ["eat","tea","tan","ate","nat","bat"]

#Time complexity: O(n*klogk) where n is the number of strings and k is the maximum length of a string in the input array. This is because we need to sort each string, which takes O(klogk) time, and we do this for all n strings.
#Space complexity: O(n*k) because in the worst case, all strings could be different and we would need to store all of them in the hashmap. Additionally, the sorted version of each string also takes O(k) space, and we have n strings, so the total space complexity is O(n*k).
#Leet code: yes

def groupAnagrams(strs):
    hashmap = {}
    for s in strs:
        temp = sorted(s)
        print(temp)
        sorted_s = ''.join(sorted(s))
        if sorted_s not in hashmap:
            hashmap[sorted_s] = [s]
        else:
            hashmap[sorted_s].append(s)
    return list(hashmap.values())
#print(groupAnagrams(strs))