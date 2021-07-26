#!/usr/local/bin/python3

import csv
import os
import sys # For mac implementation, to grab dropped argument

from pdfrw import PdfReader
from pdfrw import PdfWriter


def main(droppedFile):
    filename = os.path.basename(droppedFile)
    fold(filename)
    mag_pin(filename)
    print("done")


def fold(path):
    original = PdfReader(path)
    output = PdfWriter()
    pageCount = 0

    with open("namelist.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                if row[1] == "F/O":
                    # grab contents of row
                    page = original.pages[pageCount]
                    for x in range(int(row[2])):
                        output.addpage(page)
                pageCount += 1

    output.write("output/fold_output.pdf")


def mag_pin(path):
    original = PdfReader(path)
    output = PdfWriter()
    pageCount = 0

    with open("namelist.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                if row[1] != "F/O":
                    # grab contents of row
                    page = original.pages[pageCount]
                    for x in range(int(row[2])):
                        output.addpage(page)
                pageCount += 1

    output.write("output/mag_pin_output.pdf")


if __name__ == '__main__':
    # droppedFile = sys.argv[1]
    droppedFile = "Sample_PDF.pdf"
    print("File received")
    main(droppedFile)
