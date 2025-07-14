import unittest

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #import pdb;pdb.set_trace()
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        num_list = []
        for i in range(0, len(s)-1):
            temp_list = []
            temp_list.append(s[i])
            for j in range(i+1, len(s)):
                if s[j] not in temp_list:
                    temp_list.append(s[j])
                else:
                    #num_list.append(len(temp_list))
                    break
            num_list.append(len(temp_list))
        num_list.sort()
        
        return num_list[-1]

    def lengthOfLongestSubstring1(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        if n == 1:
            return 1
        #import pdb; pdb.set_trace()
        char_set = set()
        left = 0
        max_length = 0
        print("Initial value char_set is: ",char_set, "left is: ", left, "max length is: ", max_length)
        print("--------- Loop ----------")
        for right in range(n):
            while s[right] in char_set:
                print("enter while - left is: ", left, "s[left] is: ", s[left], "char set before removing: ", char_set)
                char_set.remove(s[left])
                left += 1
                print("in while - left is: ", left, "s[left] is: ", s[left], "char set after removing: ", char_set)
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
            print("right is: ", right, "left is: ", left, "max_length is: ", max_length, "char_set is: ", char_set)

        return max_length

s1="abcabcbb"
s2="bbbbb"
s3='a'
s4="pwwkew"

sol = Solution()
print(sol.lengthOfLongestSubstring1(s4))
