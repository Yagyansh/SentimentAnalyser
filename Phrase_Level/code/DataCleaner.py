"""This code takes as input the path of the filename of the original dataset and the output filenames.
   It returns the processed dataset with the relevant fields & The Phrases in a different file.
   It helps in generating Training Data with Labels and Testing Data(with Labels or without labels)"""

import sys


def main():
    # Check arguments
    if len(sys.argv) != 4:
        print"Usage :: python DatasetCleaner InputDataset outputFileNames"
        sys.exit(0)

    data = []
    data1 = []
    f = open(sys.argv[1], 'r')
    for line in f:
        words = line.split('\t')
        print words
        if words[5] != "Not Available\n":  # 5th index is the Actual Tweet.
            startIndex = int(words[2])
            print startIndex
            endIndex = int(words[3]) + 1
            print endIndex
            string = words[5].split(' ')
            print string
            phrase = ' '.join(string[startIndex:endIndex]).strip('\n')
            print phrase
            # data.append(line) #with labels
            if phrase != '':
                data.append(words[0] + '\t' + words[1] + '\t' + phrase + '\t' + words[4])
                data1.append(phrase)
        # data.append(words[0]+'\t'+words[3])#without labels
    f.close()

    # Write into file
    f = open(sys.argv[2], 'w')
    f.write("\n".join(data))
    f.close()

    f = open(sys.argv[3], 'w')
    f.write("\n".join(data1))
    f.close()


if __name__ == "__main__":
    main()
