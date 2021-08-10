# Word Counter:

## Part1:

Given document path (1x) with english words separated by [_], print it word count and total count

Example of ``"words.txt"`` file:

``a______bbb_c``

``c__d``

=> 

``"a 1,
bbb 1,
c  2,
d 1,
Total: 5"``

notes:
1. there are no more letters other than [a-Z,_]
2. methods should be written correctly with return values, types, etc


## Part2:

Print part 1 but in decreasing/ascending order - depend on given String ``["desc"/"asc"]``

## Part3:

Given X>1 .txt documents, do (1,2), but it should be fast.


## Look on:
1. Verify code part 1-2, Part3 just speak on design.
2. _ at start, _ at end (trim)
3. can be duplicates on code (hashmap)
4. LowerCase/UpperCase
5. Split (with _) regex? aka tokenization, what are the other options?
6. Reading / closing file - with open? Buffered in Java etc?
7. Comparator : what is it ?
8. Time complexity: let w = #of_words, O(w), sorting is neglible
9. Threads: file-per-thread VS thread-pool
10. Threads: how do you do it in Java?

**sources:**
1. Taboola mid-senior dev's home task
2. [rosettacode](https://rosettacode.org/wiki/Word_frequency)
