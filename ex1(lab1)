def caesar_cipher(text, key, decrypt=False):
    result = ""
    if decrypt:
        key = -key  # In decryption, we use the opposite key value
    for char in text:
        if 'A' <= char <= 'Z':
            shifted = ord(char) + key
            if shifted > ord('Z'):
                shifted -= 26
            result += chr(shifted)
        else:
            result += char
    return result

def main():
    choice = input("Enter 'E' to encrypt or 'D' to decrypt: ").upper()
    
    if choice == 'E':
        input_text = input("Enter the text to encrypt: ").upper()
        if input_text.isalpha():  # Check if input contains only letters
            key = int(input("Enter the key (1-25): "))
            
            if 1 <= key <= 25:
                encrypted_text = caesar_cipher(input_text, key)
                print("Encrypted text:", encrypted_text)
            else:
                print("Key must be between 1 and 25.")
        else:
            print("Only letters are allowed in the input.")
    elif choice == 'D':
        input_text = input("Enter the text to decrypt: ").upper()
        if input_text.isalpha():  # Check if input contains only letters
            key = int(input("Enter the key (1-25) for decryption: "))
            
            if 1 <= key <= 25:
                decrypted_text = caesar_cipher(input_text, key, decrypt=True)
                print("Decrypted text:", decrypted_text)
            else:
                print("Key must be between 1 and 25.")
        else:
            print("Only letters are allowed in the input.")
    else:
        print("Invalid choice. Enter 'E' to encrypt or 'D' to decrypt.")

if __name__ == "__main__":
    main()
