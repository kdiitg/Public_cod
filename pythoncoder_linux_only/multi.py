import crypt
import itertools
import threading
import time

class PasswordCracker(threading.Thread):
    def __init__(self, given_hash_password, salt, start_length, end_length):
        super().__init__()
        self.given_hash_password = given_hash_password
        self.salt = salt
        self.start_length = start_length
        self.end_length = end_length
        self.found_password = None
        self.combinations_tried = 0

    def generate_passwords(self):
        characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
#        characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>?'
        for length in range(self.start_length, self.end_length + 1):
            for combination in itertools.product(characters, repeat=length):
                password = ''.join(combination)
                yield password

    def run(self):
        start_time = time.time()
        for password in self.generate_passwords():
            hashed_password = crypt.crypt(password, self.salt)
            self.combinations_tried += 1
            if hashed_password == self.given_hash_password:
                self.found_password = password
                break
            if time.time() - start_time >= 60:
                print(f"Thread {self.ident}: Combinations tried in the last minute: {self.combinations_tried}")
                start_time = time.time()
                self.combinations_tried = 0

def main():
    given_hash_password = "$y$j9T$H0v2H3MeDpPaRiHalp3Rf.$zfMJZzpKKyeBdGg72u/I/J1crqHWlQAmXtmZSCSpTKB"
    salt = "$y$j9T$IgfQ2OeIX85NIpiWMxJq90"
    num_threads = 4
    thread_list = []

    # Split the password space evenly among threads
    passwords_per_thread = 10 ** 6 // num_threads
    start_length = 1
    for i in range(num_threads):
        end_length = min(start_length + passwords_per_thread - 1, 8)
        thread = PasswordCracker(given_hash_password, salt, start_length, end_length)
        thread_list.append(thread)
        start_length = end_length + 1

    # Start the threads
    for thread in thread_list:
        thread.start()

    # Wait for all threads to finish
    for thread in thread_list:
        thread.join()

    # Check if any thread found the password
    for thread in thread_list:
        if thread.found_password:
            print(f"Password found: {thread.found_password}")
            break
    else:
        print("Password not found")

if __name__ == "__main__":
    main()

