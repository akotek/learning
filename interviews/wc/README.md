# Word Counter:

## Part1:

Given 1x .txt document with english words separated by [_], print word count and total count

Example:

``"a______bbb_c_c__d_e"``

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

Given X>1 .txt documents, do the same, but do it fast. you can use several threads.


## Look on:
1. _ at start, _ at end
2. LowerCase/UpperCase
3. Split (with _) aka Tokenization
4. Reading / closing file
5. Data structure (hashmap) atomic
6. Thread pool

**sources:**
1. Taboola mid-senior dev's home task
2. [rosettacode](https://rosettacode.org/wiki/Word_frequency)



