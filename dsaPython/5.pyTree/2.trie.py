# TODO: implement autocomplete function in trie

'''
Trie will be binary tree of chars

Set:
    current node to root node
    current char as first char of user input word
Check:
    if current char is child of current node
        if yes:
            set current node to child node
            set current char to next char in input word
            recurse
        else:
            for all next chars in input word:
                create new node and add to trie
'''

class TrieNode:
    def __init__(self, char):

        # Char stored in this node
        self.char = char

        # Is current char end of word
        self.is_end = False

        # Counter how many times word is inserted
        self.counter = 0

        # Dictionary of child nodes
        self.children = {}


class Trie:
    def __init__(self):
        # Set root node
        self.root = TrieNode("")


    def insert(self, word):
        # Start at root
        node = self.root

        for char in word:
            if char in node.children:
                node = node.children[char]
        else:
            new_node = TrieNode(char)
            node.children[char] = new_node
            node = new_node

        # Mark end of word
        node.is_end = True

        # Increment counter to mark word
        node.counter += 1


    def dfs(self, node, prefix):
        '''
        Depth first traversal of trie

        Args:
            node        starting node
            prefix      current prefix to trace word in trie
        '''

        if node.is_end:
            self.output.append((prefix + node.char, node.counter))

        for child in node.children.values():
            self.dfs(child, prefix + node.char)


    def query(self, x):
        '''
        Given input(prefix of word):
            retrieve all words stored in trie with that prefix
            sort word by number of times inserted
        '''

        # Use variable to keep all possible values
        self.output = []
        node = self.root

        # Check if prefix in trie
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                # If prefix not found, return empty list
                return[]

        # Traverse trie for outputs
        self.dfs(node, x[:-1])

        # Sort results in reverse order and return
        return sorted(self.output, key=lambda x: x[1], reverse=True)


t = Trie()
t.insert('scallop')
t.insert('scoop')
t.insert('scum')
t.insert('salt')
t.insert('soup')
t.insert('souvee')
t.insert('slap')
t.insert('stomp')
t.query('s')