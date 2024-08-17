import crypt
import itertools
import time

def generate_passwords():
    # Define the character set to use for generating passwords
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>?'
    characters = '0123456789'
    
    # Generate all possible combinations of passwords up to length 8
    for length in range(1, 11):
        for combination in itertools.product(characters, repeat=length):
            password = ''.join(combination)
            yield password
            

def main():
    # Given hash password with salt

    given_hash_password =  "$y$j9T$H0v2H3MeDpPaRiHalp3Rf.$zfMJZzpKKyeBdGg72u/I/J1crqHWlQAmXtmZSCSpTKB"
    given_hash_password =  "$y$j9T$5qEWaMqizUexHaJHfoZnN/$hWHFV.1G53f0xaecVymAARcH1q93o9NzFNMnLYJivMC"
    salt  = "$y$j9T$IgfQ2OeIX85NIpiWMxJq90"
    salt  = "$y$j9T$5qEWaMqizUexHaJHfoZnN/"

    # Initialize a counter to track the number of combinations tried
    combinations_tried = 0
    
    # Start time
    start_time = time.time()
        
    # Generate passwords and check their hashes
    for password in generate_passwords():
        # Generate hash for the current password using the provided salt

        hashed_password = crypt.crypt(password, salt)
#        print("Hashed password with gen", hashed_password)

        
        # Compare the hashed password with the given hash password
        if hashed_password == given_hash_password:
            print(f"Password found: {password}")
            break

    
    
    
        
        # Increment the combinations tried counter
        combinations_tried += 1
        
        # Check if 1 minute has elapsed
        current_time = time.time()
        if current_time - start_time >= 60:
            print(f"Combinations tried in the last minute: {combinations_tried}")
            # Reset the start time and combinations tried counter
            start_time = current_time
            combinations_tried = 0

if __name__ == "__main__":
    main()
