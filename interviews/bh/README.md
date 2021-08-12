# Browser History Task:

1. introduction
2. coding q
3. extra (optional)
4. questions?

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

## extra:
1. What is a Primary Key, what are the benefits of using it? what is composite key? what is foreign key? what are FK useful for?
2. Streams in Java

What is printed? why?
```
List<String> ids = students.stream() 
    .filter(s - > { 
        System.out.println("filter - " + s); 
        return s.getAge() > 20; 
    })
    .map(s - > { 
        System.out.println("map - " + s); 
        return s.getName(); 
    }) 
    .limit(3) 
    .collect(Collectors.toList());
```
4. Write a function that receives a json array of urls (strings), and returns an answer whether or not all urls are currently live and responsive
5. Springframework: dependency injection? what is a framework? 
