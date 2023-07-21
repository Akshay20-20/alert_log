import re
import logging


# Regular expression

log_entry_pattern = r"\[(.*?)\] \[(.*?)\] \[(.*?)\] (.*)"

## serach for pattern and alert logging

def search_log_file(log_file_path, pattern):
    with open(log_file_path, 'r') as file:
        for line in file:
            if re.search(pattern, line):
                logging.basicConfig(filename="C:\\Users\\User\\OneDrive\\Desktop\\Python automation\\logfile.txt", level=logging.INFO)
                logging.error('Alert ! ')
                
def count_word_occurrences(log_file_path, word):
    word_count = 0

    with open(log_file_path, "r") as log_file:
        for line in log_file:
            # Split the line into words using whitespace as the delimiter
            words = line.split()
            # Count the occurrences of the word in the line
            word_count += words.count(word)

    return word_count

log_file_path = "C:\\Users\\User\\OneDrive\\Desktop\\Python automation\\logfile.txt"
search_word = "network"

result = count_word_occurrences(log_file_path, search_word)
print(f"The word '{search_word}' appears {result} times in the log file.")


log_file_path = "C:\\Users\\User\\OneDrive\\Desktop\\Python automation\\logfile.txt"
pattern = r'\bprocess request\b'  # Searching for the word
search_log_file(log_file_path, pattern)

# To extract timestamp and other properties

with open(log_file_path, "r") as log_file:
    for line in log_file:
        log_entry_pattern = r"\[(.*?)\] \[(.*?)\] \[(.*?)\] (.*)"
        log_entry_match = re.search(log_entry_pattern, line)
        if log_entry_match:
            timestamp = log_entry_match.group(1)
            severity = log_entry_match.group(2)
            component = log_entry_match.group(3)
            message = log_entry_match.group(4)
            print("Timestamp:", timestamp)
            print("Severity:", severity)
            print("Component:", component)
            print("Message:", message)
            print()  # Print a new line for separation



