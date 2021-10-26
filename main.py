#!/usr/local/bin/python3

import csv
import os
import sys # For mac implementation, to grab dropped argument

from pdfrw import PdfReader
from pdfrw import PdfWriter


def main(droppedFile):
    filename = os.path.basename(droppedFile)
    organize(filename)
    print("done")


def organize(path):
    original = PdfReader(path)
    outputFold = PdfWriter()
    outputPin = PdfWriter()
    pageCount = 0

    with open("namelist.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                page = original.pages[pageCount]
                if row[3] != "":
                    for x in range(int(row[3])):
                        outputFold.addpage(page)
                if row[2] != "":
                    for x in range(int(row[2])):
                        outputPin.addpage(page)
                if row[1] != "":
                    for x in range(int(row[1])):
                        outputPin.addpage(page)
                pageCount += 1

    outputFold.write("output/fold_output.pdf")
    outputPin.write("output/mag_pin_output.pdf")


if __name__ == '__main__':
    # droppedFile = sys.argv[1]
    droppedFile = "test.pdf"
    print("File received")
    main(droppedFile)
