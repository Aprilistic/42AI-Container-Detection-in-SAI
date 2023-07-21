import argparse


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Uploads/downloads a file to/from Dropbox.')
    # Add arguments
    parser.add_argument('--target', type=str, help='The target file that you want to convert. ex) \'/root/example\' if the target is saved as \'/root/example.txt\'')
    parser.add_argument('--type', type=str, help="The type of the target. \'.txt\' if you want to convert txt to csv. \'.csv\' otherwise.")

    # Parse the arguments
    args = parser.parse_args()

    # Access the values of the arguments
    target = args.target
    type = args.type

    with open(target) as infile:

        # Read space-delimited file and replace all empty spaces by commas
        if type == '.txt':
            data = infile.read().replace(' ', ',')
            print(data, file=open(target + '.csv', 'w'))
        else:
            data = infile.read().replace(',', ' ')
            print(data, file=open(target + '.txt', 'w'))
        # Write the CSV data in the output file