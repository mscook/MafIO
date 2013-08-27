import sys
import os
sys.path.insert(0, os.path.abspath('../MafIO'))

import MafIO

#with open('data/example.maf') as fin:
#    for line in fin:
#        print line.strip()

maf = MafIO.parse('data/example.maf')                                                   
alignment = next(maf)  # Get the next list of multiple alignments              
print len(alignment)            
