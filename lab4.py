def apply_permutation(data, permutation_table):
    return ''.join(data[i - 1] for i in permutation_table)

def left_shift(data, shift):
    return data[shift:] + data[:shift]

def generate_keys(key):
    key = key.zfill(64)
    key = apply_permutation(key, [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4])
    left_half = key[:28]
    right_half = key[28:]
    subkeys = []
    for i in range(1, 17):
        left_half = left_shift(left_half, shift_table[i - 1])
        right_half = left_shift(right_half, shift_table[i - 1])
        subkey = apply_permutation(left_half + right_half, [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32])
        subkeys.append(subkey)
    return subkeys

def apply_initial_permutation(data):
    return apply_permutation(data, [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7])

def apply_final_permutation(data):
    return apply_permutation(data, [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29, 36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25])

# User input for message and key
message = input("Enter the message (8 characters): ")
key = input("Enter the 64-bit key: ")

# Shift table
shift_table = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

# Generate subkeys
subkeys = generate_keys(key)

# Extend the message to 64 bits
extended_message = ''.join(format(ord(char), '016b') for char in message)

# Apply the initial permutation IP
permuted_message = apply_initial_permutation(extended_message)

# Choose the left half of the result of the initial permutation IP to get L1
L1 = permuted_message[:32]

print("L1:", L1)
