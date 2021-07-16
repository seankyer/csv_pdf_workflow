#!/usr/local/bin/python3
import csv
import os
import sys

def main(droppedFile):
    f = open('output/fold_output.csv', "w")
    f = open('output/mag_pin_output.csv', "w")
    filename = os.path.basename(droppedFile)
    fold(filename)
    mag_pin(filename)
    print("done")


def fold(path):
    # Open supplied csv and grab header
    with open(path) as csv_file:
        header = []
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for x in csv_reader:
            if line_count == 0:
                header.append(x)
                line_count += 1

    # Open output csv and write header
    with open('output/fold_output.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header[0])

        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    if row[1] == "F/O":
                        # grab contents of row
                        entry = [row[0], row[1], row[2], row[3], row[4]]
                        for x in range(int(row[2])):
                            # write contents to the csv (.writerow() automatically selects the next available line)
                            writer.writerow(entry)


def mag_pin(path):
    # Open supplied csv and grab header
    with open(path) as csv_file:
        header = []
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for x in csv_reader:
            if line_count == 0:
                header.append(x)
                line_count += 1

    # Open output csv and write header
    with open('output/mag_pin_output.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header[0])

        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    if row[1] == "M" or "P":
                        # grab contents of row
                        entry = [row[0], row[1], row[2], row[3], row[4]]
                        for x in range(int(row[2])):
                            # write contents to the csv (.writerow() automatically selects the next available line)
                            writer.writerow(entry)


if __name__ == '__main__':
    #droppedFile = sys.argv[1]
    droppedFile = "SampleFile.csv"
    print("File recieved")
    main(droppedFile)
