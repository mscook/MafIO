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
    """
    Elements of the Sequence object:
    
        * src  = (strain) 
        * start
        * size
        * strand
        * srcSize
        * text (seq)

    *src:* can be database.chromosome or strain or reference

    """

    def __init__(self, line):
        data = line.strip().split()
        if len(data) != 7:
            print data
            raise Exception('Does not conform to MAF spec')
        try:
            self.species, self.chr = data[1].split('.')
        except ValueError:
            tmp = data[1].split('.')
            if len(tmp) == 1:
                self.species = tmp
                self.strain = self.species
                self.chr = None
            else:
                self.species = tmp[0]
                self.strain = self.species
                self.chr = None
        self.start = int(data[2])
        self.size = int(data[3])
        self.strand = data[4]
        self.chrsize = int(data[5])
        self.srcSize = self.chrsize
        self.seq = data[6]
        self.text = self.seq

def parse(handle):
    """
    Parse the MAF file
   
    Please see: http://genome.ucsc.edu/FAQ/FAQformat#format5 for the MAF 
    format specification

    'a ' = Alignment Block Lines
    's ' = Sequence within an alignment block
    'i ' = information about the context of the sequence lines immediately 
           preceeding them
    'e ' = information about empty parts of the alignment block
    'q ' = information about the quality of each aligned base for the 
           species/strain
    
    :param handle: the file handle object to the MAF file

    :returns: iterator that return a group of alignemnt sequence objects every 
              time you call it with next()
    """
    if not isinstance(handle, str):
        raise TypeError('Need a string for file name.')

    with open(handle, 'r') as fi:
        # Check the 1st and second record identify as a MAF
        if not contains_header(fi.readline()):
            if not contains_header(fi.readline()):
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


def contains_header(line):
    """
    Ensure that the MAF file contains a header

    Header is defined as: ##maf version=1 scoring=tba.v8 
    """
    rv = False
    if line.find('##maf') != -1:
        rv = True
    return rv
