class Blockchain:
    class Block:
        # Represents a single block in the blockchain. Each block contains an ID, data, and a type.
        def __init__(self, block_id, data, block_type):
            self.id = block_id
            self.data = data
            self.type = block_type
            self.next = None
            self.prev = None

    # A doubly linked list implementation of a simple blockchain. Supports efficient insertion at the end and reverse traversal.
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        # Returns True if the blockchain is empty. Time complexity: O(1)
        return self.head is None

    def add(self, block_id, data, block_type):
        # Appends a new block to the end of the chain. Time complexity: O(1)
        new_block = self.Block(block_id, data, block_type)

        if self.head is None:
            self.head = self.tail = new_block
        else:
            self.tail.next = new_block
            new_block.prev = self.tail
            self.tail = new_block

    def delete(self, block_id):
        # Deletes the block with the given ID, if found. Time complexity: O(n)
        current = self.head

        while current:
            if current.id == block_id:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next  # Removing head

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev  # Removing tail
                print(f"Deleted id: {current.id}, data: {current.data}, type: {current.type}")
                del current
                return True
            current = current.next
        print(f"Could not delete id:{block_id}  ID not found")
        return False  # Block not found

    def find(self, block_id):
        # Searches for and prints the block with the specified ID. Time complexity: O(n)
        current = self.head
        while current:
            if current.id == block_id:
                print(f"ID: {current.id}, Data: {current.data}, Type: {current.type}")
                return current
            current = current.next

        print(f"ID {block_id} not found.")
        return None

    def print_chain(self):
        # Prints all blocks in forward order. Time complexity: O(n)
        print("------Printing in forward direction-------")

        current = self.head
        while current:
            print(f"ID: {current.id}, Data: {current.data}, Type: {current.type}")
            current = current.next

    def print_chain_reverse(self):
        # Prints all blocks in reverse order. Time complexity: O(n)
        print("------Printing in reverse direction-------")

        current = self.tail
        while current:
            print(f"ID: {current.id}, Data: {current.data}, Type: {current.type}")
            current = current.prev

    def sort_by_type(self, block_type):
        # In-place partition: group matching type first, preserve order, O(n) time
        if not self.head or not self.head.next:
            print(f"List sorted with {block_type} first.")
            return

        # Pointers for two lists
        match_head = match_tail = None
        other_head = other_tail = None
        current = self.head

        while current:
            nxt = current.next
            # Detach
            current.prev = current.next = None

            if current.type == block_type:
                if not match_head:
                    match_head = match_tail = current
                else:
                    match_tail.next = current
                    current.prev = match_tail
                    match_tail = current
            else:
                if not other_head:
                    other_head = other_tail = current
                else:
                    other_tail.next = current
                    current.prev = other_tail
                    other_tail = current

            current = nxt

        # Combine lists
        if match_tail:
            match_tail.next = other_head
            if other_head:
                other_head.prev = match_tail
            self.head = match_head
            self.tail = other_tail or match_tail
        else:
            self.head = other_head
            self.tail = other_tail

        print(f"List sorted with {block_type} first.")


def main():
    chain = Blockchain()
    filePath = "testCase3.txt"
    try:
        f = open(filePath, "r", encoding="utf-8")
    except:
        print(f"File not found: {filePath}")
        return

    with f:
        for line in f:
            parts = line.strip().split()
            if not parts:
                continue  # skip empty lines

            cmd = parts[0]

            if cmd == "A" and len(parts) == 4:
                # A id data type
                block_id = parts[1]
                data = parts[2]
                block_type = parts[3]
                chain.add(block_id, data, block_type)

            elif cmd == "R" and len(parts) == 2:
                # R id
                removed = chain.delete(parts[1])
                if not removed:
                    print(f"No block with ID '{parts[1]}' to remove.")

            elif cmd == "F" and len(parts) == 2:
                # F id
                chain.find(parts[1])

            elif cmd == "P":
                chain.print_chain()

            elif cmd == "PR":
                chain.print_chain_reverse()

            elif cmd == "S" and len(parts) == 2:
                chain.sort_by_type(parts[1])

            else:
                print(f"Invalid command: {line.strip()}")

main()
