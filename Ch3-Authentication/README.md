# Activity I

Hardware Specification
- **CPU** : Apple M1 Max
- **RAM** : 32 GB
- **OS**: macOs 14.0

## 1. Write a simple python program to use the word from the dictionary to find the original value of d54cc1fe76f5186380a0939d2fc1723c44e8a5f7. Note that you might want to include substitution in your code (lowercase, uppercase, number for letter [‘o’ => 0 , ‘l’ => 1, ‘i’ => 1]).

```python
import hashlib
import itertools
import time
import json
import os

def substitute_characters(word):
	"""Create a list of possible substitutions for a given word"""
	character_mapping = {
	"a": ["a", "A", "4"],
	"b": ["b", "B", "8"],
	"c": ["c", "C"],
	"d": ["d", "D", "6"],
	"e": ["e", "E", "3"],
	"f": ["f", "F"],
	"g": ["g", "G", "9"],
	"h": ["h", "H"],
	"i": ["i", "I", "1"],
	"j": ["j", "J"],
	"k": ["k", "K"],
	"l": ["l", "L", "1"],
	"m": ["m", "M"],
	"n": ["n", "N"],
	"o": ["o", "O", "0"],
	"p": ["p", "P"],
	"q": ["q", "Q", "9"],
	"r": ["r", "R"],
	"s": ["s", "S"],
	"t": ["t", "T"],
	"u": ["u", "U"],
	"v": ["v", "V"],
	"w": ["w", "W"],
	"x": ["x", "X"],
	"y": ["y", "Y"],
	"z": ["z", "Z", "2"],
	}
	# Create a list of lists where each inner list contains possible characters for each position in the word
	char_options = [character_mapping.get(char, [char]) for char in word]
	possible_combinations = [
	"".join(combination) for combination in itertools.product(*char_options)
	]
	return possible_combinations

def find_original_value(hash_value, dictionary_path="./10k-most-common.txt"):
"""Find the original value of a hash by comparing it to a dictionary of passwords"""
start_time = time.time()

with open(dictionary_path, "r") as dictionary:
	for line in dictionary:
		word = line.strip()
		# Create a list of possible substitutions for each character in the word
		possible_combinations = substitute_characters(word)
		for combination in possible_combinations:
			# Hash the combination and compare it to the target hash
			cracker_hash = hashlib.sha1(combination.encode()).hexdigest()
			if cracker_hash == hash_value:
				end_time = time.time()
				print(f"Found the password: {combination}")
				print(f"Time taken: {end_time - start_time} seconds")
				return
		
		end_time = time.time()
		
		print(f"Password not found. Time taken: {end_time - start_time} seconds")
  
def create_rainbow_table(dictionary_path):
	"""Create a rainbow table of hashes and their original values"""
	start_time = time.time()
	rainbow_table = {}
	with open(dictionary_path, "r") as dictionary:
		for line in dictionary:
			word = line.strip()
			possible_combinations = substitute_characters(word)
			for combination in possible_combinations:
				hash_value = hashlib.sha1(combination.encode()).hexdigest()
				rainbow_table[hash_value] = combination
	
	end_time = time.time()
	print(f"Time taken to create rainbow table: {end_time - start_time} seconds")
	
	# Saving the rainbow table to a file
	with open("rainbow_table.json", "w") as file:
		json.dump(rainbow_table, file)
	
	# Measuring the size of the file
	file_size = os.path.getsize("rainbow_table.json")
	print(f"Size of rainbow table file: {file_size} bytes")
	
	return rainbow_table
```

## 2. For the given dictionary, create a rainbow table (including the substituted strings) using the sha1 algorithm. Measure the time for creating such a table. Measure the size of the table
- Time taken to create rainbow table: 6.6741838455200195 seconds
- Number of entries in rainbow table: 8187947
- Size of rainbow table file: 484187077 bytes or 461.75678 MB

## 3. Based on your code, how long does it take to perform a hash (sha1) on a password string? Please analyze the performance of your system
- Time taken to hash a word: 4.0531158447265625e-06 seconds

## 4. If you were a hacker obtaining a password file from a system, estimate how long it takes to break a password with brute force using your computer. (Please based the answer on your measurement from exercise #3.)
- Assuming the password has 8 characters long and the password only contains lowercase letters, uppercase letters, or numbers. The total number of possible combinations is (26 + 26 + 10)^8 = 218,340,105,584,896. Time taken for hashing a password is about 4.0e-6 seconds so it will take 873360422.3 seconds or 27.67 years.

## 5. Base on your analysis in exercise #4, what should be the proper length of a password. (e.g. Take at least a year to break).
- From the previous question,  8 characters long and the password only contains lowercase letters, uppercase letters, or numbers seem to be a strong password in this case since it takes years to break. Therefore, to be more confidence on the password ,longer password is secure more than the shorter one (>8 characters).

## 6. What is salt? Please explain its role in protecting a password hash
- Salt is a cryptographic concept used to enhance the security of stored passwords. It's essentially a random string that is added to a user's password before the password is hashed.

