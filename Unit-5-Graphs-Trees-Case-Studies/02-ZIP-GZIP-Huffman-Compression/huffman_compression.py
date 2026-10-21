import heapq
from collections import Counter


class HuffmanNode:
    def __init__(self, char=None, frequency=0, left=None, right=None):
        self.char = char
        self.frequency = frequency
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.frequency < other.frequency


class HuffmanCoding:
    def build_tree(self, text):
        frequency = Counter(text)

        if not frequency:
            return None, frequency

        heap = [
            HuffmanNode(char, freq)
            for char, freq in frequency.items()
        ]
        heapq.heapify(heap)

        if len(heap) == 1:
            only_node = heapq.heappop(heap)
            root = HuffmanNode(
                frequency=only_node.frequency,
                left=only_node
            )
            return root, frequency

        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)

            merged = HuffmanNode(
                frequency=left.frequency + right.frequency,
                left=left,
                right=right
            )

            heapq.heappush(heap, merged)

        return heap[0], frequency

    def generate_codes(self, root):
        codes = {}

        if root is None:
            return codes

        def traverse(node, code):
            if node.char is not None:
                codes[node.char] = code if code else "0"
                return

            traverse(node.left, code + "0")

            if node.right is not None:
                traverse(node.right, code + "1")

        traverse(root, "")
        return codes

    def encode(self, text, codes):
        return "".join(codes[char] for char in text)

    def decode(self, encoded_text, root):
        if root is None:
            return ""

        decoded = []
        current = root

        for bit in encoded_text:
            if bit == "0":
                current = current.left
            else:
                current = current.right

            if current.char is not None:
                decoded.append(current.char)
                current = root

        return "".join(decoded)

    def compress(self, text):
        root, frequency = self.build_tree(text)
        codes = self.generate_codes(root)
        encoded = self.encode(text, codes) if text else ""
        return encoded, codes, frequency, root


def display_frequency_table(frequency):
    print("\n--- Character Frequencies ---")
    for char, count in sorted(
        frequency.items(),
        key=lambda item: (-item[1], item[0])
    ):
        display_char = repr(char)
        print(f"{display_char:8} : {count}")


def display_codes(codes):
    print("\n--- Huffman Codes ---")
    for char, code in sorted(codes.items(), key=lambda item: item[0]):
        print(f"{repr(char):8} : {code}")


def main():
    huffman = HuffmanCoding()

    print("===== ZIP/GZIP Style Huffman Compression Demo =====")
    text = input("Enter text to compress: ")

    if not text:
        print("Empty input cannot be compressed.")
        return

    encoded, codes, frequency, root = huffman.compress(text)

    display_frequency_table(frequency)
    display_codes(codes)

    decoded = huffman.decode(encoded, root)

    original_bits = len(text) * 8
    compressed_bits = len(encoded)

    print("\n--- Compression Result ---")
    print("Original text:", text)
    print("Encoded bits:", encoded)
    print("Original size:", original_bits, "bits")
    print("Encoded data size:", compressed_bits, "bits")

    if original_bits:
        ratio = compressed_bits / original_bits * 100
        print(f"Encoded data is {ratio:.2f}% of the original character-bit size.")

    print("\n--- Verification ---")
    print("Decoded text:", decoded)
    print("Compression/decompression successful:", decoded == text)


if __name__ == "__main__":
    main()
