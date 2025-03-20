
###########################

def first_non_repeating_char(word):
    seen={}
    for l in word:
        if l not in seen:
            seen[l]=1
        else:
            seen[l]+=1
    for item, count in seen.items():
        if count ==1:
            return item



print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )



"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""