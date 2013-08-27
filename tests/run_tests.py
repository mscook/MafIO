import sys
import os
sys.path.insert(0, os.path.abspath('../MafIO'))

import MafIO

maf = MafIO.parse('data/example.maf')
alignment = next(maf)  # Get the next list of multiple alignments
for e in alignment:
    print e.seq
