# Name: ...
# CSE 140
# Homework 2: DNA analysis

# This program reads DNA sequencer output and computes statistics, such as
# the GC content.  Run it from the command line like this:
#   python dna_analysis.py myfile.fastq


###########################################################################
### Libraries
###

# The sys module supports reading files, command-line arguments, etc.
import sys


###########################################################################
### Read the nucleotides into a variable named seq
###

# You need to specify a file name
if len(sys.argv) < 2:
    print("You must supply a file name as an argument when running this program.")
    sys.exit(2)
# The file name specified on the command line, as a string.
filename = sys.argv[1]
# A file object from which data can be read.
inputfile = open(filename)

# All the nucleotides in the input file that have been read so far.
seq = ""
# The current line number (= the number of lines read so far).
linenum = 0


for line in inputfile:
    linenum = linenum + 1
    # if we are on the 2nd, 6th, 10th line...
    if linenum % 4 == 2:
        # Remove the newline characters from the end of the line
        line = line.rstrip()
        seq = seq + line


###########################################################################
### Compute statistics
###

# Total nucleotides seen so far.
total_count = 0
# Number of G and C nucleotides seen so far.
gc_count = 0
# Number of A and T nucleotides seen so far.
at_count = 0
# Number of G nucleotides seen so far.
g_count = 0
# Number of C nucleotides seen so far.
c_count = 0
# Number of A nucleotides seen so far.
a_count = 0
# Number of T nucleotides seen so far.
t_count = 0

# for each base pair in the string,
for bp in seq:
    # increment the total number of bps we've seen
    total_count = total_count + 1

    # next, if the nucleotide is a C,
    if bp == 'C':
        # increment the count of C, also update GC count
        c_count = c_count + 1
        gc_count = gc_count + 1

    # next, if the nucleotide is a G,
    if bp == 'G':
        # increment the count of gc, also update GC count
        g_count = g_count + 1
        gc_count = gc_count + 1

    # next, if the nucleotide is a A,
    if bp == 'A':
        # increment the count of A, also update AT count
        a_count = a_count + 1
        at_count = at_count + 1

    # next, if the nucleotide is a T,
    if bp == 'T':
        # increment the count of T, also update AT count
        t_count = t_count + 1
        at_count = at_count + 1

# added sum_count to use below to get AT and GC content
sum_count = g_count + c_count + a_count + t_count

# divide the gc_count by the total_count
# gc_content = float(gc_count) / total_count
# changed total_count to sum_count because gc content did not match expected
gc_content = float(gc_count) / sum_count

# divide the at_count by the total_count
# at_content = float(at_count) / total_count
# changed total to sum  because at content did not match expected
at_content = float(at_count) / sum_count

# divide at count by gc count to
at_gc_ratio = float(at_count) / gc_count

# for GC content categorization
for gc in range(1):
    if gc_content > .6:
        gc_category = "high GC content"
    elif gc_content < .4:
        gc_category = "low GC content"
    else:
        gc_category = "moderate GC content"

# Print the answer
print('GC-content:', gc_content)
print('AT-content:', at_content)
print('G-count:', g_count)
print('C-count:', c_count)
print('A-count:', a_count)
print('T-count:', t_count)
print('Sum count:', g_count + c_count + a_count + t_count)
print('Total count:', total_count)
print('Sequnce length:', len(seq))
print('AT/GC ratio:', at_gc_ratio)
print('GC Class:', gc_category)