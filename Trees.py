class Node:
    def __init__(self, value):
        self.value=value
        self.right=None
        self.left=None

class BinarySearchTree:
    def __init__(self):
        self.root=None

    def insert(self, value):
        new_node=Node(value)
        if self.root is None:
            self.root=new_node
            return True
        temp=self.root
        while (True):
            if new_node.value==temp.value:
                return False
            if new_node.value>temp.value:
                if temp.right is None:
                    temp.right=new_node
                    return True
                temp=temp.right
            if new_node.value<temp.value:
                if temp.left is None:
                    temp.left=new_node
                    return True
                temp=temp.left

    def contains(self,value):
        temp=self.root
        while temp is not None:
            if temp.value==value:
                print("found")
                return True
            elif value>temp.value:
                temp=temp.right
            elif value<temp.value:
                temp=temp.left

        print("not found")
        return False

                

        
        


my_binary_tree=BinarySearchTree()
my_binary_tree.insert(4)
my_binary_tree.insert(5)
my_binary_tree.insert(3)



# print(my_binary_tree.root.value)
# print(my_binary_tree.root.left.value)
my_binary_tree.contains(1)