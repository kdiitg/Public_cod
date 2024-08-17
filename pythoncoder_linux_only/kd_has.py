import hashlib

def generate_hash(text):
    # Encode the text to bytes (UTF-8 encoding is common)
    encoded_text = text.encode('utf-8')
    
    # Create a hashlib object for SHA-256
    hash_object = hashlib.sha256()
    
    # Update the hash object with the encoded text
    hash_object.update(encoded_text)
    
    # Get the hexadecimal representation of the hash
    hashed_text = hash_object.hexdigest()
    
    return hashed_text

# Example usage
text = "Hello, World!"
hashed_value = generate_hash(text)
print(f"Hash value for '{text}' is: {hashed_value}")
