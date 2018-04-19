"""This code combines the output of the tokeniser and the input tweet set and returns the final
   input file in the format : tweet Id, Tweet tokens, POS tokens,label """

import sys
from itertools import izip


def main():
    # Check Arguments
    if len(sys.argv) != 4:
        print "Usage :: python combine.py ProcessedDataset TokenisedDataset FinalDataset"
        sys.exit(0)

    # Combine both the files.
    data = []
    f1 = open(sys.argv[1], 'r')
    f2 = open(sys.argv[2], 'r')
    for line1, line2 in izip(f1, f2):
        words1 = line1.strip().split('\t')
        words2 = line2.strip().split('\t')
        if len(words1) == 4 and len(words2) == 4:
            string = words1[0] + '\t' + words2[0] + '\t' + words2[1] + '\t' + words1[3] + '\n'
            data.append(string)
    f1.close()
    f2.close()

    # Write into File
    f = open(sys.argv[3], 'w')
    f.write("".join(data))
    f.close()


if __name__ == "__main__":
    main()
