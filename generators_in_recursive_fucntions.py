import string
from operator import itemgetter

# yield from is used in recursive functions

class BstNode:
    def __init__(self, word, word_sum):
        self.left = None
        self.right = None
        self.node_word = word
        self.node_sum = word_sum

    def bst_insert(self, root, new_node):
        if root is None:
            return new_node
        else:
            if root.node_sum <= new_node.node_sum:
                if root.right is None:
                    root.right = new_node
                else:
                    self.bst_insert(root.right, new_node)
            else:
                if root.left is None:
                    root.left = new_node
                else:
                    self.bst_insert(root.left, new_node)
            return root

    def inorder(self, root):
        if root:
            yield from self.inorder(root.left)
            yield (root.node_word)
            yield from self.inorder(root.right)


characters = dict()
words = []

cnt = 1

for character in string.ascii_lowercase:
    characters[character] = cnt
    cnt += 1

input_string = input().lower().split()

new_clean_string_with_one_space = ""
for i in input_string:
    new_clean_string_with_one_space += i
    new_clean_string_with_one_space += " "

temp_word_summer = 0
temp_word = ""
for i in new_clean_string_with_one_space:
    if i == " ":
        words.append([temp_word, temp_word_summer])
        temp_word_summer = 0
        temp_word = ""
    else:
        temp_word += i
        temp_word_summer += characters[i]

# root node
root = BstNode(words[0][0], words[0][1])
root = root.bst_insert(None, root)

for i in range(1, len(words)):
    new_node = BstNode(words[i][0], words[i][1])
    root = root.bst_insert(root, new_node)

answer = ""

for i in root.inorder(root):
    answer += i
    answer += " "

print("Answer string : {answer}".format(answer=answer))