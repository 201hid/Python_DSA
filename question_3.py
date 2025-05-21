# import sys
# for line in sys.stdin:
#     max_word=''
#     for word in line.strip().split():
#         if len(word)>len(max_word):
#             max_word=word
#     print(max_word)



from collections import defaultdict

import sys
for line in sys.stdin:
    words= line.strip().split()
    length=defaultdict(list)

    for word in words:
        length[len(word)].append(word)
    
    max_word=max(length.keys())
    print(length[max_word][0])

