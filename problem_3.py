import sys

class Node:
    def __init__(self, key, value):
    self.key = key
    self.value = value
    self.left = left
    self.right = right
    
class Tree:
    def __init__(self, root):
        self.root = root
    
#calculate frequency of each character in the dataset
def char_freq(data):
    freq = dict()
    for char in data:
        freq[char] = freq.get(char) + 1
    return freq
    
def sort_freq(data):
    items = list(data.items())
    #lambda arguments : expression
    items.sort(key=lambda x: x[1])
    return items
        
def add_n_to_l(node, sorted_list):
    if not sorted_list:
        return node
    for index, val in enumerate(sorted_list):
        if node.value < val.value:
            sorted_list.insert(index, node)
            break
        sorted_list.append(node)
        break
        
def encode_tree(root, e_string, e_dict):
    if(root.right is None and root.left is None):
        e_dict[root.key] = e_string
    else:
        if(root.left is not None):
            encode_tree(root.left, e_string + "0", e_dict)
        if(root.right is not None):
            encode_tree(root.right, e_string + "1", e_dict)
            
def decode_tree(data, root, index, d_string):
    if(root.right is None and root.left is None):
        d_string += root.key
        return index, d_string
    elif(data[index] == "0"):
        return decode_tree(data, root.left, index + 1, d_string)
    else:
        return decode_tree(data, root.right, index + 1, d_string)
    
def huffman_encoding(data):
    #if there is no data/data is empty
    if not data:
        return None
            
    freq = char_freq(data)
    sorted_freq = sort_freq(freq)
    node_sorted = list(map(lambda x: Node(x[0], x[1]), sorted_freq))
    tree = None
        
    while len(node_sorted) > 1:
        first_ele = node_sorted.pop(0)
        sec_ele = node_sorted.pop(0)
        sum_ele = first_ele.value + sec_ele.value
        root_node = Node(sum_ele, sum_ele)
        root_node.left = first_ele
        root_node.right = sec_ele
        add_n_to_l(root_node, node_sorted)
        if not node_sorted:
            tree = Tree(root_node)
    
    if tree is None:
        if len(node_sorted) == 1:
            first_ele = node_sorted.pop(0)
            tree = Tree(Node(first_ele.value, first_ele.value))
            tree.root.left = Node(first_ele.key, first_ele.value)
            
    e_char = dict()
    encode_tree(tree.root, "", e_char)
    e_str = ""
    for value in data:
        e_str += e_char[value]
    return e_str, tree
    
def huffman_decoding(data, root):
    if(root is None):
        return data
        
    index = 0
    d_str = ""
    while((index + 1) <= len(data)):
        index, d_str = decode_tree(data, root, index, d_str)
    return d_str
    
#Test

def test_cases(text):
    
    print ("The size of the data is: {}\n".format(sys.getsizeof(text)))
    print ("The content of the data is: {}\n".format(text))
    
    encoded_data, tree = huffman_encoding(text)
    
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    
test_cases('')
test_cases('Test')
test_cases('Test case number three')  
