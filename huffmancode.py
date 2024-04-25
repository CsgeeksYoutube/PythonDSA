import heapq
from collections import defaultdict

class Node:
    def __init__(self, symbol=None, weight=0, left=None, right=None):
        self.symbol = symbol
        self.weight = weight
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.weight < other.weight

def build_huffman_tree(frequencies):
    # heap = [Node(symbol, weight) for symbol, weight in frequencies.items()]
    heap = []
    for symbol, weight in frequencies.items():
        node = Node(symbol, weight)
        heap.append(node)
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        combined_weight = left.weight + right.weight
        combined_node = Node(left=left, right=right, weight=combined_weight)
        heapq.heappush(heap, combined_node)

    return heap[0]


def generate_huffman_codes(node, prefix="", codes={}):

    if node.symbol is not None:
        codes[node.symbol] = prefix
    
    if node.left is not None:
        generate_huffman_codes(node.left, prefix + "0", codes)
    
    if node.right is not None:
        generate_huffman_codes(node.right, prefix + "1", codes)
    
    return codes


def huffman_coding(data):
    if not data:
        return {}

    frequency = defaultdict(int)
    for symbol in data:
        frequency[symbol] += 1

    huffman_tree = build_huffman_tree(frequency)
    huffman_codes = generate_huffman_codes(huffman_tree)

    return huffman_codes

data = "aabbcaaddbbbaaaddeddeff"
codes = huffman_coding(data)

print("Symbol".ljust(10) + "Huffman Code")
for symbol, code in codes.items():
    print(symbol.ljust(10) + code)
