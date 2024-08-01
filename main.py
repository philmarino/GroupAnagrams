def groupAnagrams(strs):
    output = dict()
    for word in strs:
        key = ''.join(sorted(word))
        if key in output.keys():
            temp = output.get(key)
            temp.append(word)
            output.update({key : temp})
            #output.update({key : output.get(key).append(word)})
        else:
            output.update({key : [word]})

    return output.values()

# Example 1:
# Input: 
strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:
# Input: 
strs = [""]
print(groupAnagrams(strs))
# Output: [[""]]

# Example 3:
# Input: 
strs = ["a"]
print(groupAnagrams(strs))
# Output: [["a"]]
