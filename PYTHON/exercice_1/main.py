import csv
import re
import os
import sys

INPUT_PATH = "./input/ip_adresses.txt"
OUTPUT_BASE_PATH = "./output"
OUTPUT_CORRECT_ADRS = os.path.join(OUTPUT_BASE_PATH, 'correct_ips.txt')
OUTPUT_INCORRECT_ADRS = os.path.join(OUTPUT_BASE_PATH, 'incorrect_ips.txt')

ADRS_REGEX = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"

compiled_regex = re.compile(ADRS_REGEX)

def main():
    """Split corrects and incorrects IP adresses from an input file
    Args: None
    Returns: None
    """
    if not os.path.isfile(INPUT_PATH):
        print("File path {} does not exist. Exiting...".format(INPUT_PATH))
        sys.exit()

    correct_file = open(OUTPUT_CORRECT_ADRS, 'w')
    incorrect_file = open(OUTPUT_INCORRECT_ADRS, 'w')

    with open(INPUT_PATH, 'rb') as txtFile:
        for line in txtFile:
            adrs = line.strip()
            result = compiled_regex.match(adrs)
            if result:
                correct_file.write(line)
            else:
                incorrect_file.write(line)



if __name__ == '__main__':
    main()