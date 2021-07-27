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
                for x in range(int(row[2])):
                    if row[1] == "F/O":
                        outputFold.addpage(page)
                    elif row[1] != "F/O":
                        outputPin.addpage(page)
                pageCount += 1

    outputFold.write("output/fold_output.pdf")
    outputPin.write("output/mag_pin_output.pdf")


if __name__ == '__main__':
    # droppedFile = sys.argv[1]
    droppedFile = "Sample_PDF.pdf"
    print("File received")
    main(droppedFile)
