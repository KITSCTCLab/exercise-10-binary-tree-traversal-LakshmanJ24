class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def insert(root, new_value) -> BinaryTreeNode:
    """If binary search tree is empty, make a new node, declare it as root and return the root.
        If tree is not empty and if new_value is less than value of data in root, add it to left subtree and proceed recursively.
        If tree is not empty and if new_value is >= value of data in root, add it to right subtree and proceed recursively.
        Finally, return the root.
        """
    # Write your code here


def inorder(self,root) -> None:
    # Write your code here
    res=[]
    if root:
        res=self.inorderTraversal(root.left_child)
        res.append(root.data)
        res=res + self.inorderTraversal(root.right_child)
    return res


def preorder(self,root) -> None:
    # Write your code here
    res = []
    if root:
        res.append(root.data)
        res=res + self.PreorderTraversal(root.left_child)
        res=res + self.PreorderTraversal(root.right_child)
    return res


def postorder(root) -> None:
    # Write your code here
    res=[]
    if root:
        res=self.PostorderTraversal(root.left_child)
        res=res + self.PostorderTraversal(root.right_child)
        res.append(root.data)
    return res


# Do not change the following code
input_data = input()
flag = True
root = None
for item in input_data.split(', '):
    if flag is True:
        root = insert(None, int(item))
        flag = False
    else:
        insert(root, int(item))
inorder(root)
print()
preorder(root)
print()
postorder(root)
