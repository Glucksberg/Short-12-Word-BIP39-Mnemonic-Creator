# Short 12-Word BIP39 Mnemonic Generator

Creates mnemonics with short words that is easy to store and use.
This script generates very short and very long mnemonic phrases and checks their lengths.
The repetitive number of same-size mnemonics is due to multiprocessing and poor script design.

## Installation

Run the following command to install required packages:
pip install -r requirements.txt

than

Execute the script:
python seed5.py

have fun


## Script Analysis

Importing Required Libraries:
The script imports Mnemonic from the mnemonic library, time for tracking the duration of operations, and Pool from multiprocessing to handle parallel processing.

The generate_and_check Function:
This function generates mnemonic phrases with a strength of 128 bits, which typically results in a 12-word phrase.
It checks the length of each generated phrase and prints out the phrase and the time taken to generate it if it's the first of its kind (based on length).

Parallel Processing:
The find_first_mnemonics function sets up a pool of worker processes (one less than the number of CPU cores) to run generate_and_check concurrently.
This parallel processing aims to increase the efficiency of generating unique mnemonic phrases.

Continuous Execution:
The script is designed to run indefinitely, constantly generating and checking new mnemonic phrases in parallel.
Execution Flow:

When the script is executed, it calls find_first_mnemonics, which then continuously runs the generate_and_check function in multiple processes.
