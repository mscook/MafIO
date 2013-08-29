MafIO-Banzai
============

This module if for reading MAF files. The Banzai pipeline was originally 
using what looks to be an abandoned fork of BioPython with MAF support 
(https://github.com/polyatail/biopython/tree/alignio-maf). This pollutes and 
complicates installation/distribution of Banzai.

We also only use the MAF files from mugsy. Mugsy conveniently does not 
follow the MAF specification (see next). **This MAF parser is tailored to 
mugsy MAF** and the name should probably show this.

More info on MAF files can be found at 
https://genome.ucsc.edu/FAQ/FAQformat.html#format5

The original *basic/buggy* implementation this is based on is at:
https://github.com/jlhg/MafIO


Usage
-----

Given a MAF file such like::

    ##maf version=1 scoring=autoMZ.v1
    a score=22996.000000
    s dm3.chrXHet       224 308 +   204112 tagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagataga
    s droSim1.chrX 11606526 308 - 17042790 TCGAAAAATGGTAAAATTTAAAAATTTTTAGCTGGGGATGTTACGCGATAGAAAATTACatagaaagatagatagatagataaatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagatagataga
    i droSim1.chrX N 0 C 0


This module provides parse function to generate an iterator that return a
group of alignemnts objects and corresponding sequence objects in the 
alignment every time you call it (next).


Example usage
-------------

.. code:: python

    import MafIO

    input_strains  = 36
    LCB_cutoff     = 5000

    maf = MafIO.parse('data/example3.maf')
    headers, concat  = [], []
    # Iterate over all multiple alignments
    for alignment in maf.next():
        cur = alignment.sequences
        if len(cur) == input_strains:
            if len(cur[0]) >= LCB_cutoff:
                 # Iterate over all sequences in given alignment
                for i, seqs in enumerate(alignment.sequences):
                    # Won't be in first iteration
                    if '>'+seqs.species not in headers:
                        headers.append('>'+seqs.species)
                        concat.append(seqs.seq)
                    else:
                        concat[i] = concat[i]+seqs.seq

    with open("example.fsa", "w") as fout:
        for idx, e in enumerate(headers):
            fout.write(e+'\n')
            fout.write(concat[idx]+'\n')

