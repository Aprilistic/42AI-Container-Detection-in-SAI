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

    with open(target + type) as infile:

        if type == '.txt':
            data = "File,Confidence,X1,Y1,X2,Y2,X3,Y3,X4,Y4\n"
            for line in infile:
                columns = line.strip().split(' ')
                columns[0] = columns[0][:8]
                new_line = ','.join(columns)
                new_line += '\n'
                data += new_line
            print(data, file=open(target + '.csv', 'w'))
        else:
            data = infile.read().replace(',', ' ')
            print(data, file=open(target + '.txt', 'w'))