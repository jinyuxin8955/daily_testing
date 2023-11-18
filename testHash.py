import hashlib

def calculate_hash(data):
    hash_object = hashlib.sha256(data.encode())
    return hash_object.hexdigest()

input_data = "Hello, World!"

original_hash = calculate_hash(input_data)
print(original_hash)

modified_input_data = input_data + " "
modified_hash = calculate_hash(modified_input_data)
print(modified_hash)

hash_if_match = original_hash == modified_hash
print(hash_if_match)
