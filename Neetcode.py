def groupAnagrams( strs: list[str]) -> list[list[str]]:
        index=0
        output=[]
        while index < len(strs):
            first_word= strs[index]
            y = index+1
            while y < len(strs):
                  second_word=strs[y]
                  if isanagram(strs[index], strs[y]):
                    output.append(first_word)
                    output.append(second_word)
                    print(output)
                  y = y+1
            # print("")      
            index= index +1      


def isanagram(strs_one, strs_two):

    dict_for_one={}
    dict_for_two={}
    if len(strs_one)==len(strs_two):
            for i in strs_one:
                if i in dict_for_one:
                    dict_for_one[i]= dict_for_one[i] +1
                else:
                    dict_for_one[i]=1
            for i in strs_two:
                if i in dict_for_two:
                    dict_for_two[i]= dict_for_two[i] +1
                else:
                    dict_for_two[i]=1
            if dict_for_two == dict_for_one:
                return True
            
    else:
         return False
    

strs = ["act","pots","tops","cat","stop","hat"]

groupAnagrams(strs)
