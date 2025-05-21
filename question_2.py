# import sys
# for line in sys.stdin:
#     words = line.strip().split()
#     capitalized = [word[0].upper() + word[1:] if word else '' for word in words]
#     print(" ".join(capitalized)	)
#     # print('    '.join(capitalized))




















import sys
for line in sys.stdin:
    words= line.strip().split()
    capped=[words[0].upper()+words[:1]if words else '' for word in words]
    print('', capped)