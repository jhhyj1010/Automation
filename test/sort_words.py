#!/usr/bin/env python3
from collections import Counter, defaultdict
import typing

def groupAnagrams(strs: typing.List[str]) -> typing.List[typing.List[str]]:
    word_flag: typing.Dict[str, bool] = {}
    results: typing.List[typing.List[str]] = []
    if len(strs) == 1 or all(s == '' for s in strs) or all(len(s) == 1 for s in strs):
        return [strs]

    for i in range(0, len(strs)):
        if word_flag.get(strs[i], False):
            continue
        tmp_list: typing.List[str] = []
        if strs[i] not in tmp_list and not word_flag.get(strs[i], False):
            tmp_list.append(strs[i])
            word_flag[strs[i]] = True
        for j in range(i+1, len(strs)):
            if (Counter(strs[i]) == Counter(strs[j]) and strs[i] != strs[j]) and (strs[j] not in word_flag):
                tmp_list.append(strs[j])
                word_flag[strs[j]] = True
        results.append(tmp_list)
    return results

def groupAnagrams_copilot(strs: typing.List[str]) -> typing.List[typing.List[str]]:
    anagrams = defaultdict(list)
    
    for word in strs:
        sorted_word = ''.join(sorted(word))
        print(word)
        print(sorted_word)
        print('.......')
        anagrams[sorted_word].append(word)
    print(anagrams.values())
    return list(anagrams.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
#strs = ["ant", "ant"]
print(groupAnagrams_copilot(strs))
