MafIO-Banzai
============

This module if for reading MAF files. The Banzai pipeline was originally 
using what looks to be an abandoned fork of BioPython with MAF support 
(https://github.com/polyatail/biopython/tree/alignio-maf). This pollutes and 
complicates installation/distribution of Banzai.

More info on MAF files can be found at 
https://genome.ucsc.edu/FAQ/FAQformat.html#format5


Issues
------

** Assumes only a single alignment. See more below. **


Usage
-----

Given a MAF file such like::

    ##maf version=1 scoring=autoMZ.v1
    a score=22996.000000
    s dm3.chrXHet       224 308 +   204112 tagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagataga
    s droSim1.chrX 11606526 308 - 17042790 TCGAAAAATGGTAAAATTTAAAAATTTTTAGCTGGGGATGTTACGCGATAGAAAATTACatagaaagatagatagatagataaatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagataga
    i droSim1.chrX N 0 C 0


Tis module provides parse function to generate an iterator that return a
group of alignemnt sequence objects every time you call it (next).

```
>>> import MafIO
>>> maf = MafIO.parse('dro.maf')
>>> alignment = next(maf)  # Get the next list of multiple alignments
>>> len(alignment)
2  # There are two sequences in this list
>>> aln = alignment[0]  # Get the first sequence
>>> aln.species
'dm3'  # Species name
>>> aln.chr
'chrXHet' # Chromosome name
>>> aln.start
224  # The start of the aligning region
>>> aln.size
308  # The size of the aligning region (without gap)
>>> aln.strand
'+'  # Sequence strand
>>> aln.chrsize
204112  # Chromosome length
>>> aln.seq
'tagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatag
atagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagataga'  # Alignment sequence
```
