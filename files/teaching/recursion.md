---
title: 'CS111 Recursion Lab'
date: 2024-10-28
permalink: /recursion/
layout: singlefull
---

## Setup
Download the starter code file [here](https://github.com/annapmeyer/annapmeyer.github.io/raw/refs/heads/anna/files/teaching/recursion.py). 

Solve the following exercises with a partner. 

## Exercise 0: Palindromes
We discussed this example together. Re-implement the code and discuss the questions with a partner to check your understanding.

A palindrome is a word or phrase that reads the same forwards and backwards. For instance, "racecar" and "madam" are palindromes. 

Write a recursive function that checks whether a string is a palindrome. 

* What is the base case?
* If a string has length *n*, how many recursive calls will there be?
* **Challenge:** What if you want to also check whether phrases are palindromes, ignoring spaces, punctuation, and capitalization? For instance, "A man, a plan, a canal - Panama" is a palindrome under this paradigm.

## Exercise 1: Reversing a string
I want to convert a string to be read backwards. For instance, "hello" should become "olleh". 

Write a function to do this recursively. 

## Exercise 2: Nested list target matching
Suppose that I have a *nested list*. Each entry in the list is either an integer or another list. For instance,
`[[1, 2, 3], 4, [5, 6, 7], 8]` is a nested list with 2 levels. We want to write a function `nested_list(lst, target)` that checks whether a target integer is in the list or any of its sub-list. For instance, the function would return True for the example list with target=1 or target=4, but false for target=9. 

You will write two functions for this problem, and discuss the related questions.
1. Write the code for `nested_list_depth_2`. This is an *iterative* function (i.e., using a `for` or `while` loop) that checks whether a target integer is in a nested list with up to two levels.
* How would you have to modify this function to solve the problem for a list with up to 3 levels? Is this scalable as the list gets deeper?

2. Write a *recursive* function that checks whether a target integer is in a nested list of any depth.
* What is the base case?
* How many recursive calls are there for the input `[1, [2, 3], [4, [5, 6, [7, 8], 9], [10, 11]], 12]`? 


## Exercise 3: Triangular numbers

The nth triangular number is the sum 1 + .... + n. For instance, the 5th triangular number is 15 = 1 + 2 + 3 + 4 + 5. Write a function to recursively compute the nth triangular number.


## Exercise 4: Fibonacci sequence
The Fibonacci sequence is defined as 0, 1, 1, 2, 3, 5, 8, 13, .... That is, given the starting values $F_0$=0 and $F_1$=1, the nth Fibonacci number for $n\geq 2$ is $F_n=F_{n-1} + F_{n-2}$. 

Write a recursive function to compute the nth Fibonacci number. 

## Exercise 5: Binary to decimal (Challenge!)

Given a string of 0's and 1's, convert it to a base-ten integer. For instance, `base_two_base_ten("10")` should return 2, and `base_two_base_ten("10110")` should return 22. Hint: do a few examples by hand and consider how you can break the problem into smaller sub-steps.

* What is the base case? 
* For a string of length *n*, how many recursive calls will you do?



