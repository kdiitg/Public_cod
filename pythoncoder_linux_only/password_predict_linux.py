import crypt
import itertools
import time

# Define the character set to use for generating passwords
#characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>?'
characters = 'abcdefgmnZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>?'
#characters = '0123456789'
#given_hash_password =  "$y$j9T$pkpZmp1cO74meM7icrxCd1$h3sPXHd4C4qNRbmCS2HKf2BWudOkR8X3HRWMvd3RJj5"
#given_hash_password =  "$y$j9T$IgfQ2OeIX85NIpiWMxJq90$jlS/c9EOvDBy2X/TvWE.5pnBY00ZlX5GmM5UyfwYhc/"#mint:                1 
#given_hash_password =  "$y$j9T$pkpZmp1cO74meM7icrxCd1$h3sPXHd4C4qNRbmCS2HKf2BWudOkR8X3HRWMvd3RJj5"#poweruser:           2   
#given_hash_password =  "$y$j9T$8D1KBOUS2/koaT4E6Ep3G/$k7Xgc/U/BSU/yyNHIp1b2efqx3dDH8kSKXqrosgLgo0" #poweruser1:         2  
#given_hash_password =  "$y$j9T$OkQhNIIBW8J3jxQSBP22D/$vHyqxXV0oVvyKbzdoxx2PZcaPthJfjF1vFXnJ5Dy5ED" #poweruser2:         25
#given_hash_password =  "$y$j9T$RJufa6UXKSqlE5mnwbNvS0$0z8nNs923dmoapTkgcJoFtB6YcnZeMIQn11HNT18Pn." #amit:               25 
given_hash_password =  "$y$j9T$ZmuAdutEg3ucegI42Cw0a0$LbE3ieBEJcpYZdvFw06kpsNYuiUlqHlIuwEgsDVWaI8" #testuser1:           25




salt = '$'.join(given_hash_password.split("$")[0:4])
print(salt)

def generate_passwords():
    
    # Generate all possible combinations of passwords up to length 8
    for length in range(1, 11):
        for combination in itertools.product(characters, repeat=length):
            password = ''.join(combination)
            yield password
            

def main():
    # Given hash password with salt

#    given_hash_password = input('Enter Hash Value of password: ')
    

#    salt  = "$y$j9T$8D1KBOUS2/koaT4E6Ep3G/"

    # Initialize a counter to track the number of combinations tried
    combinations_tried = 0
    
    # Start time
    start_time = time.time()
        
    # Generate passwords and check their hashes
    for password in generate_passwords():
        # Generate hash for the current password using the provided salt


        hashed_password = crypt.crypt(password, salt)
#        print("Hashed password with gen", hashed_password, password)
#        time.sleep(.5)
        
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
