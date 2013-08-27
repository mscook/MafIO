# Copyright (C) 2013, Jian-Long Huang
# Licensed under The MIT License
# http://opensource.org/licenses/MIT
#
# Author: Jian-Long Huang (jianlong@ntu.edu.tw)
# Version: 0.1
# Created: 2013.5.5
#
# This module is for reading the MAF file:
# https://genome.ucsc.edu/FAQ/FAQformat.html#format5


class Sequence:

    def __init__(self, line):
        data = line.split()
        self.species, self.chr = data[1].split('.')
        self.start = int(data[2])
        self.size = int(data[3])
        self.strand = data[4]
        self.chrsize = int(data[5])
        self.seq = data[6]


def parse(handle):

    if not isinstance(handle, str):
        raise TypeError('Need a string for file name.')

    with open(handle, 'r') as fi:
        if fi.readline()[0:5] != '##maf':
            raise Exception('Need MAF format file.')

        maf_container = []

        for line in fi:
            if line[0] == 's':
                maf_container.append(Sequence(line.rstrip('\n')))
            elif line[0] == '\n':
                yield maf_container
                maf_container = []
            else:
                pass
