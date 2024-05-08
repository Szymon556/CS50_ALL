import csv
from sys import argv


def main():

    if(len(argv)!=3):

        print("Źle podane wartości")

        exit(1)

    with open(argv[1],"r") as file:

        reader = csv.DictReader(file)


        dict = list(reader)
    
    with open(argv[2],"r") as f:

        input = f.read()


    matches = {}

    for x in dict[0]:
        if x != 'name':

            matches[x] = longest_match(input,x)


    counter = 0

    for i in range(len(dict)):
        for j in matches:

            if str(matches[j]) == str(dict[i][j]):
                counter = counter + 1

        if counter == len(matches):

            print(dict[i]['name'])
            break
        else:
            counter = 0


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
