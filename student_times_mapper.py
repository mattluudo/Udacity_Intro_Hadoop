#!/usr/bin/python
import sys
import csv

def mapper(stdin):
	reader = csv.reader(sys.stdin, delimiter='\t')
	header = 1
	for line in reader:
		# Skip if header
		if header == 1:
			header = 0
			continue
		# Check data integreity
		if len(line) != 19:
			continue
		# Extract needed data
		author_id, hr_added_at = line[3], line[8][11:13]
		yield("{0}\t{1}".format(author_id, hr_added_at))

def main():
	for output in mapper(sys.stdin):
		print(output)

if __name__ == "__main__":
	main()

