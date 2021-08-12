# Browser History Task:

## part 1:
We would like to build functionality of a ```one-tab-browser``` where you start on **the homepage**, can **visit** another url, get **back/forward** (1 or more steps) and **know your current url** (can be empty). 

Implement the ```BrowserHistory class```, write code on IDEA (does not have to compile, and in any language).

## part 2:
Extend the solution to multi-tabs

## part3:
Support persistence - if user refreshes, back/forward are still functional

## notes:
1. what is stack, what are other data structures we have [linked list, arraylist], how they work in Java?
2. edge case: when you back/visit - now forward history should be reseted (code in "visit" function should have that), steps>0 validation
3. options to solve Q: [linked_list, 2x stacks LIFO, array with idx]
4. BrowserHistory(), visit(String url), back(int steps), forward(int steps), status()
5. Persistence: Disk/DB? DB ```Table1[session_id, history(json-data structure)]``` Disk: write both stacks to File (each file == tab == session)

source: [leetcode](https://leetcode.com/problems/design-browser-history/)
