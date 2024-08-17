import crypt

password = "1"

# Generate the hash using SHA-512 encryption
hashed_password = crypt.crypt(password, crypt.mksalt(crypt.METHOD_SHA512))

print("Hashed password:", hashed_password)


# Define the password
password = "1"

# Generate the hash using crypt.crypt()
# The salt "$6$j9TIgfQ2OeIX85NI$" is extracted from the provided hash
# You may need to extract it from the hash programmatically for different hashes
salt = "$6$j9TIgfQ2OeIX85NI$"
hashed_password = crypt.crypt(password, salt)

print("Hashed password with given salt $6$j9TIgfQ2OeIX85NI$:", hashed_password)

salt2  = "$y$j9T$IgfQ2OeIX85NIpiWMxJq90"
hashed_password = crypt.crypt(password, salt2)

print("Hashed password with given salt $y$j9T$IgfQ2OeIX85NIpiWMxJq90:", hashed_password)

