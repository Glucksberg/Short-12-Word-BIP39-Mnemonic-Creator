from mnemonic import Mnemonic
import time
from multiprocessing import Pool
import os

def generate_and_check(start_time, phrase_lengths):
    mnemo = Mnemonic("english")
    local_phrase_lengths = set(phrase_lengths)  # Local copy to store found lengths
    while True:
        words = mnemo.generate(strength=128)
        phrase_length = len(words)
        if phrase_length not in local_phrase_lengths:
            elapsed_time = time.time() - start_time
            local_phrase_lengths.add(phrase_length)
            print(f"First found for {phrase_length} characters: '{words}' (found in {elapsed_time:.2f} seconds)")

def find_first_mnemonics():
    start_time = time.time()
    num_processes = os.cpu_count() - 1
    phrase_lengths = set()  # Set to store lengths of phrases found

    with Pool(num_processes) as pool:
        for _ in range(num_processes):
            pool.apply_async(generate_and_check, [start_time, phrase_lengths])

        # Keep the main process running indefinitely
        while True:
            time.sleep(1)

if __name__ == '__main__':
    find_first_mnemonics()
