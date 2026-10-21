class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    # Hash function
    def hash_function(self, word):
        hash_value = 0

        for char in word:
            hash_value += ord(char)

        return hash_value % self.size

    # Insert word and meaning
    def insert(self, word, meaning):
        index = self.hash_function(word)

        # Update meaning if the word already exists
        for pair in self.table[index]:
            if pair[0] == word:
                pair[1] = meaning
                print("Word updated successfully!")
                return

        self.table[index].append([word, meaning])
        print("Word inserted successfully!")

    # Search word
    def search(self, word):
        index = self.hash_function(word)

        for pair in self.table[index]:
            if pair[0] == word:
                return pair[1]

        return None

    # Delete word
    def delete(self, word):
        index = self.hash_function(word)

        for pair in self.table[index]:
            if pair[0] == word:
                self.table[index].remove(pair)
                print("Word deleted successfully!")
                return

        print("Word not found!")

    # Display hash table
    def display(self):
        print("\n--- Hash Table ---")

        for i in range(self.size):
            print(f"Bucket {i}: ", end="")

            if not self.table[i]:
                print("Empty")
            else:
                for word, meaning in self.table[i]:
                    print(f"[{word}: {meaning}]", end=" -> ")
                print("None")


def main():
    dictionary = HashTable()

    while True:
        print("\n===== Dictionary Application =====")
        print("1. Insert Word")
        print("2. Search Word")
        print("3. Delete Word")
        print("4. Display Hash Table")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            word = input("Enter word: ").strip().lower()
            meaning = input("Enter meaning: ").strip()
            dictionary.insert(word, meaning)

        elif choice == "2":
            word = input("Enter word to search: ").strip().lower()
            meaning = dictionary.search(word)

            if meaning is not None:
                print(f"Meaning of '{word}': {meaning}")
            else:
                print("Word not found!")

        elif choice == "3":
            word = input("Enter word to delete: ").strip().lower()
            dictionary.delete(word)

        elif choice == "4":
            dictionary.display()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
