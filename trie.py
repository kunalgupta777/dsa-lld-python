import random


class TrieNode:
    def __init__(self, val=None):
        self.val = val
        self.children = {chr(97+i): None for i in range(26)}
        self.is_word = None

def insert_word(root: TrieNode, word: str) -> None:
    curr_node = root
    word = word.lower()
    for w in word:
        if not curr_node.children[w]:
            new_node = TrieNode(val=w)
            curr_node.children[w] = new_node
        curr_node = curr_node.children[w]
    curr_node.is_word = True

def build_trie(words: list[str]) -> TrieNode:
    root = TrieNode()
    for word in words:
        insert_word(root=root, word=word)
    print("Trie built successfully!")
    return root

def search_prefix(root: TrieNode, prefix: str) -> any:
    curr = root
    for c in prefix:
        c = c.lower()
        if not curr.children[c]:
            return False
        curr = curr.children[c]
    return curr

def search_word(root: TrieNode, word: str) -> bool:
    resp = search_prefix(root, word)
    if resp == False:
        return False
    return resp.is_word

def generate_words(count=1000):
    word_list = []
    characters = [chr(97+i) for i in range(26)] + [chr(97+i).upper() for i in range(26)]
    for i in range(count):
        word_length = random.randint(10, 50)
        word = "".join(random.choices(characters, k=word_length))
        word_list.append(word)
    print("Generated " + str(count) + " words!")
    return word_list

if __name__ == "__main__":
    word_list = generate_words()
    root = build_trie(words=word_list[:len(word_list)-100])

    exists_count = 0
    not_exists_count = 0
    for word in word_list[len(word_list)-200:]:
        if search_word(root=root, word=word):
            print(word + " exists in Trie")
            exists_count += 1
        else:
            print(word + " doesn't exist in Trie")
            not_exists_count += 1
    print("Exist Count", exists_count)
    print("Doesn't Exist Count", not_exists_count)
    







