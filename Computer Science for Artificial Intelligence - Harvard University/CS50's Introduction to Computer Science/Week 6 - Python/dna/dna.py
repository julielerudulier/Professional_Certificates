import csv
import sys


def main():
    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Error - please enter names of files")

    # TODO: Read database file into a variable
    file_1 = sys.argv[1]
    names = []
    with open(file_1) as db:
        reader1 = csv.DictReader(db)
        for name in reader1:
            names.append(name)

    # TODO: Read DNA sequence file into a variable
    file_2 = sys.argv[2]
    dna_sequence = []
    with open(file_2) as dna:
        reader2 = csv.reader(dna)
        for row in reader2:
            dna_sequence.append(row)
    sequence = dna_sequence[0]

    # TODO: Find longest match of each STR in DNA sequence
    for i in range(len(names)):
        tmp_dict = names[i]
        all_keys = list(tmp_dict.keys())
        filtered_keys = all_keys[1:]

    match_counts = []
    for key in filtered_keys:
        match = longest_match(sequence[0], key)
        match_counts.append(match)

    # TODO: Check database for matching profiles
    length_db = len(names)

    for i in range(length_db):
        tmp = names[i]
        find_match = [i for i in tmp.values()]
        find_match = find_match[1:]
        find_match = [int(i) for i in find_match]
        if find_match == match_counts:
            print(tmp["name"])
            return
    if find_match != match_counts:
        print("No match")
        return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):
        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:
            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
