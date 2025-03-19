# two dict

# def find_duplicates(list1):
#     seen={}
#     duplicates={}
#     for i in list1:
#         if i not in seen:
#             seen[i]=True
#         else:
#             if i not in duplicates:
#                 duplicates[i]=True
#     return list(duplicates.keys())
            
        

def find_duplicates(list1):
    seen = {}
    duplicates = []

    for i in list1:
        if i in seen:
            seen[i] += 1
        else:
            seen[i] = 1

    for element, count in seen.items():
        if count > 1:
            duplicates.append(element)

    return duplicates

print(find_duplicates([1, 2, 3, 4, 5]))
print(find_duplicates([1, 1, 2, 2, 3]))
print(find_duplicates([1, 1, 1, 1, 1]))
print(find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]))
print(find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]))
print(find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]))
print(find_duplicates([]))

