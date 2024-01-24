import hashlib
import itertools
import time


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
                print(f"Checking {combination}...")
                # Hash the combination and compare it to the target hash
                cracker_hash = hashlib.sha1(combination.encode()).hexdigest()
                if cracker_hash == hash_value:
                    end_time = time.time()
                    print(f"Found the password: {combination}")
                    print(f"Time taken: {end_time - start_time} seconds")
                    return

    end_time = time.time()
    print(f"Password not found. Time taken: {end_time - start_time} seconds")


target_hash = "d54cc1fe76f5186380a0939d2fc1723c44e8a5f7"
find_original_value(target_hash)
