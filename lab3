class VigenereCipher:
    def __init__(self, alphabet):
        self.alphabet = alphabet.upper()
        self.matrix = self._create_matrix()

    def _shift_row(self, input_string, n):
        n = n % len(input_string)
        return input_string[n:] + input_string[:n]

    def _create_matrix(self):
        return [self._shift_row(self.alphabet, i) for i in range(len(self.alphabet))]

    def _extend_key(self, string, key):
        quotient, remainder = divmod(len(string), len(key))
        return quotient * key + key[:remainder]

    def _get_indexes(self, string):
        return [self.alphabet.index(char) for char in string]

    def _validate_input(self, string):
        return all(char in self.alphabet for char in string)

    def encrypt_decrypt(self, key, string, operation):
        key = key.replace(' ', '').upper()
        string = string.replace(' ', '').upper()

        if not (self._validate_input(key) and self._validate_input(string)):
            print('Invalid input. Use letters from the specified alphabet only.')
            return

  
        extended_key = self._extend_key(string, key)
        key_indexes = self._get_indexes(extended_key)
        string_indexes = self._get_indexes(string)

        if operation == 'encrypt':
            return ''.join(self.matrix[k][v] for k, v in zip(key_indexes, string_indexes))
        elif operation == 'decrypt':
            return ''.join(self.alphabet[(v-k) % len(self.alphabet)] for k, v in zip(key_indexes, string_indexes))
        else:
            print('Invalid operation. Choose "encrypt" or "decrypt".')
            return


def menu():
    alphabet = 'AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ'
    cipher = VigenereCipher(alphabet)

    while True:
        print("e for Encryption ")
        print("d for Decryption")

    
        choice = input("Choose an option: ")

       
        if choice == "e":
            key = input("Enter the key: ")
            string_to_encrypt = input("Enter the message to encrypt: ")
            encrypted_message = cipher.encrypt_decrypt(key, string_to_encrypt, 'encrypt')
            print(f'Encrypted message: {encrypted_message}')
        elif choice == "d":
            key = input("Enter the key: ")
            string_to_decrypt = input("Enter the message to decrypt: ")
            decrypted_message = cipher.encrypt_decrypt(key, string_to_decrypt, 'decrypt')
            print(f'Decrypted message: {decrypted_message}')
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == '__main__':
    menu()
