'''
This file is used to crawl current data from imdb datasets.
'''

import urllib.request
import urllib.parse
import magic
import csv
import gzip

name_file, name_header = urllib.request.urlretrieve('https://datasets.imdbws.com/name.basics.tsv.gz')

print(magic.from_file(name_file))  # see what file type it is. From imdb databse, the file should be tsv file

with gzip.open(name_file, 'r') as f:
    file = f.read()

#file = open(name_file)
read_tsv = csv.reader(file, delimiter="\t")

x = 0

while x < 10:
    for row in read_tsv:
        print(row)
        x += 1

file.close()
