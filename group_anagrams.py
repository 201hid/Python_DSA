def group_anagrams(word_list):
    anagram={}
    for word in word_list:
        sortedword=''.join(sorted(word))
        if sortedword not in anagram:
            anagram[sortedword]=[]
        anagram[sortedword].append(word)

    return list(anagram.values())


 



print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

# print("\n2nd set:")
# print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

# print("\n3rd set:")
# print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )



"""
    EXPECTED OUTPUT:
    ----------------
    1st set:
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    2nd set:
    [['abc', 'cba', 'bac'], ['foo'], ['bar']]

    3rd set:
    [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]

"""