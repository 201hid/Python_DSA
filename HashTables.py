class HashTables:
    def __init__(self, size =7):
        self.data_map= [None]*size




    def __hash__(self, key):
        my_hash = 0
        for letter in key:
            my_hash= (my_hash +ord(letter)*23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i,":", val)

    def insert(self, key, value):
        index= self.__hash__(key)
        if self.data_map[index] is None:
            self.data_map[index]=[]
        self.data_map[index].append([key,value])

    def get(self, key):
        index= self.__hash__(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map)):
                if self.data_map[index][i][0]==key:
                    return self.data_map[index][i][1]
        return None
    
    def keys(self):
        all_keys=[]
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in self.data_map[i]:
                    all_keys.append(self.data_map[i][0])
        return all_keys


# my_hashtable = HashTables()

# # my_hashtable.print_table()

# my_hashtable.insert("ball", 5)
# my_hashtable.insert("bat", 2)
# my_hashtable.insert("player", 11)
# # my_hashtable.print_table()

# print(my_hashtable.get("player"))

# print(my_hashtable.keys())

list1=[1,2,3]
list2=[2,3,4]
def item_in_common(list1, list2):
    dict={}
    for i in list1:
        dict[i]=True
    for y in list2 :
        if y in dict:
            return True
    return Falsealse

