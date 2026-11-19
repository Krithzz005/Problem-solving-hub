import os
import heapq
import pickle
import sys

class HuffmanNode:
    def __init__(self, byte, freq):
        self.byte = byte
        self.freq = freq
        self.left = None
        self.right = None

    # Define comparison operators for the greedy min-heap priority queue
    def __lt__(self, other):
        return self.freq < other.freq

class FileZipper:
    def __init__(self):
        self.codes = {}
        self.reverse_codes = {}

    def _build_frequency_map(self, data):
        """Phase 1: Count frequency of each byte."""
        freq_map = {}
        for byte in data:
            freq_map[byte] = freq_map.get(byte, 0) + 1
        return freq_map

    def _build_huffman_tree(self, freq_map):
        """Phase 2: Greedy assembly of the Huffman Tree using a priority queue."""
        heap = []
        for byte, freq in freq_map.items():
            node = HuffmanNode(byte, freq)
            heapq.heappush(heap, node)

        # Handle file with only 1 unique character
        if len(heap) == 1:
            node = heapq.heappop(heap)
            root = HuffmanNode(None, node.freq)
            root.left = node
            heapq.heappush(heap, root)

        while len(heap) > 1:
            node1 = heapq.heappop(heap)
            node2 = heapq.heappop(heap)

            merged = HuffmanNode(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2

            heapq.heappush(heap, merged)

        return heapq.heappop(heap)

    def _build_codes_helper(self, root, current_code):
        """Phase 3: Traverse tree recursively to build binary bitstrings."""
        if root is None:
            return

        if root.byte is not None:
            self.codes[root.byte] = current_code
            self.reverse_codes[current_code] = root.byte
            return

        self._build_codes_helper(root.left, current_code + "0")
        self._build_codes_helper(root.right, current_code + "1")

    def _build_codes(self, root):
        self.codes = {}
        self.reverse_codes = {}
        self._build_codes_helper(root, "")

    def _pack_bits(self, data):
        """Phase 4: Convert '0101' bitstring into real, memory-saving bytes."""
        bit_string = "".join(self.codes[byte] for byte in data)
        
        # Calculate padding needed to make length a multiple of 8
        extra_padding = 8 - (len(bit_string) % 8)
        if extra_padding == 8:
            extra_padding = 0
            
        bit_string += "0" * extra_padding
        
        # Convert bitstring segments to actual bytes
        compressed_bytes = bytearray()
        for i in range(0, len(bit_string), 8):
            byte_segment = bit_string[i:i+8]
            compressed_bytes.append(int(byte_segment, 2))
            
        return bytes(compressed_bytes), extra_padding

    def compress(self, input_path, output_path):
        """Compresses any binary or text file."""
        if not os.path.exists(input_path):
            print(f"Error: File '{input_path}' not found.")
            return

        with open(input_path, 'rb') as f:
            data = f.read()

        if not data:
            print("Error: Empty file cannot be compressed.")
            return

        freq_map = self._build_frequency_map(data)
        root = self._build_huffman_tree(freq_map)
        self._build_codes(root)
        compressed_bytes, padding = self._pack_bits(data)

        # Bundle the compressed payload along with metadata needed to unpack it
        payload = {
            'freq_map': freq_map,
            'padding': padding,
            'data': compressed_bytes
        }

        with open(output_path, 'wb') as f:
            pickle.dump(payload, f)
            
        orig_size = os.path.getsize(input_path)
        comp_size = os.path.getsize(output_path)
        print(f"Successfully Compressed!")
        print(f"Original Size: {orig_size} bytes")
        print(f"Compressed Size: {comp_size} bytes")
        print(f"Space Saved: {((orig_size - comp_size) / orig_size) * 100:.2f}%")

    def decompress(self, input_path, output_path):
        """Decompresses a previously zipped file back to its original state."""
        if not os.path.exists(input_path):
            print(f"Error: File '{input_path}' not found.")
            return

        with open(input_path, 'rb') as f:
            payload = pickle.load(f)

        freq_map = payload['freq_map']
        padding = payload['padding']
        compressed_bytes = payload['data']

        # Rebuild the identical tree from the saved frequency metadata
        root = self._build_huffman_tree(freq_map)
        self._build_codes(root)

        # Convert bytes back into a bit string of '0' and '1'
        bit_string = "".join(f"{byte:08b}" for byte in compressed_bytes)
        
        # Strip away the extra padding bits added during compression
        if padding > 0:
            bit_string = bit_string[:-padding]

        # Decode bit string using the tree maps
        decompressed_bytes = bytearray()
        current_code = ""
        for bit in bit_string:
            current_code += bit
            if current_code in self.reverse_codes:
                decompressed_bytes.append(self.reverse_codes[current_code])
                current_code = ""

        with open(output_path, 'wb') as f:
            f.write(decompressed_bytes)
            
        print(f"Successfully Decompressed to '{output_path}'!")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage:")
        print("  Compression:   python zipper.py compress <input_file> <output_file.huff>")
        print("  Decompression: python zipper.py decompress <compressed_file.huff> <output_file>")
        sys.exit(1)

    action = sys.argv[1].lower()
    src = sys.argv[2]
    dest = sys.argv[3]

    zipper = FileZipper()
    if action == "compress":
        zipper.compress(src, dest)
    elif action == "decompress":
        zipper.decompress(src, dest)
    else:
        print("Invalid action. Use 'compress' or 'decompress'.")
