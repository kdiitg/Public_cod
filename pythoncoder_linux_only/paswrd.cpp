#include <iostream>
#include <string>
#include <cmath>

bool crackPassword(const std::string& hash, int passwordLength) {
  // Define the character set (digits 1 to 9)
  const std::string characters = "123456789";

  // Iterate through all combinations of digits
  for (int i = 0; i < std::pow(characters.size(), passwordLength); ++i) {
    std::string guess;
    int digitIndex = i;

    // Convert integer counter to password string (base conversion)
    for (int j = 0; j < passwordLength; ++j) {
      guess.insert(0, 1, characters[digitIndex % characters.size()]);
      digitIndex /= characters.size();
    }

    // Simulate password hashing (replace with actual hashing function)
    std::string hashedGuess = "Hashed_" + guess;

    // Compare hashed guess with actual hash
    if (hashedGuess == hash) {
      std::cout << "Password found: " << guess << std::endl;
      return true;
    }
  }

  std::cout << "Password not found within " << std::pow(characters.size(), passwordLength) << " tries." << std::endl;
  return false;
}

int main() {
  // Replace with actual hashed password
  std::string hash = "HashedPassword";
  int passwordLength = 1; // Adjust for desired password length

  // Call the crackPassword function
  crackPassword(hash, passwordLength);

  return 0;
}

