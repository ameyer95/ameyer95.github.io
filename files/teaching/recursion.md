---
title: 'CS111 Recursion Lab'
date: 2024-10-28
permalink: /recursion/
layout: singlefull
---

## Setup
Access the starter code [here](https://github.com/annapmeyer/annapmeyer.github.io/raw/refs/heads/anna/files/teaching/recursion.py). You will need to copy and paste the code into your own file.

Solve the following exercises with a partner. 

## Exercise 0: Palindromes
We discussed this example together. Re-implement the code and discuss the questions with a partner to check your understanding.

A palindrome is a word or phrase that reads the same forwards and backwards. For instance, "racecar" and "madam" are palindromes. 

Write a recursive function that checks whether a string is a palindrome. 

* What is the base case?
* If a string has length *n*, how many recursive calls will there be?

## Exercise 1: Triangular numbers

For $n\geq 1$, the $n$th triangular number is the sum $1 + .... + n$. For instance, the 5th triangular number is $15 = 1 + 2 + 3 + 4 + 5$. Write a function to recursively compute the $n$th triangular number. 

*Hint:* If $T_k$ is the $k$th triangular number, how would you write the $(k+1)$st triangular number, $T_{k+1}$?

* What is the base case?
* How is this function different from `factorial_recursive()` that we talked about at the start of class?

## Exercise 2: Reversing a string
I want to convert a string to be read backwards. For instance, "hello" should become "olleh". 

Write a function to do this recursively. 

* What is the base case? (*Hint:* what is the reverse of `"a"`? What about of `""`?) 
* What is the recursive case?

## Exercise 3: Nested list target matching
Suppose that I have a *nested list*. Each entry in the list is either an integer or another list. For instance,
`[[1, 2, 3], 4, [5, 6, 7], 8]` is a nested list with 2 levels. We want to write a function `nested_list(lst, target)` that checks whether a target integer is in the list or any of its sub-lists. For instance, the function would return True for the example list with target=1 or target=4, but false for target=9. 

1. Look at the code for `nested_list_depth_2`. This is an *iterative* function (i.e., uses a `for` or `while` loop) that checks whether a target integer is in a nested list with up to two levels.
* How would you have to modify this function to solve the problem for a list with up to 3 levels, e.g., `[1, [2, [3, 4], 5], 6]`? Is this modification scalable for lists that are arbitrarily deep?

2. Write a recursive function that checks whether a target integer is in a nested list of any depth. *Hint:* You are allowed to use a loop, as long as you also use recursion. 

* What is the base case? (*Hint:*  What would a function called `nested_list_depth_1` look like?)
* How many recursive calls are there for the input `[1, [2, 3], [4, [5, 6, [7, 8], 9], [10, 11]], 12]`? 


## Exercise 4: Fibonacci sequence
The Fibonacci sequence is defined as 0, 1, 1, 2, 3, 5, 8, 13, .... That is, given the starting values $F_0$=0 and $F_1$=1, the *n*th Fibonacci number for $n\geq 2$ is $F_n=F_{n-1} + F_{n-2}$. 

Write a recursive function to compute the *n*th Fibonacci number, for $n\geq 0$. 

*Hint:* You may want to include more than one base case.

*Hint:* You may want to include multiple recursive calls. 

*Note:* Writing this function is a good way to practice recursion, but it turns out this function is very slow when $n$ is too large (on Anna's computer, it noticeably slows down when $n>25$ and stops working when $n>35$). You will learn more on Wednesday about why this is, and what is a better way to compute the Fibonacci numbers!  

## Exercise 5: Binary to decimal (Challenge!)

Behind the scenes, computer code is compiled to *binary*, i.e., base-2 numbers that are strings of 0's and 1's. For instance, `"10"` represents 2 and `"101"` represents 5. 

Recall that we can decompose *decimal* (base 10) numbers to be written as powers of 10. For instance, 2345 can be written as $2\times 10^3 + 3\times 10^2 + 4 \times 10^1 + 5\times 10^0$. 

Likewise, we can convert a binary string to base 10 by writing it as a sum of powers of 2. For instance, 

* `"10"`$= 1 \times 2^1 + 0 \times 2^0 = 2$
* `"101"`$= 1 \times 2^2 + 0 \times 2^1 + 1 \times 2^0$
*  `"1010111"`$= 1\times 2^6 + 0 \times 2^5 + 1\times 2^4 + 0 \times 2^3 + 1\times 2^2 + 1\times 2^1 + 1\times 2^0 = 64 + 16 + 4  + 2 + 1 = 87$

Write a function to convert a binary string of 0's and 1's to a base-ten integer using recursion. 

* What is the base case? (*Hint:* What numbers are written the same in base 10 and base 2?)
* What is the recursive call? (How are you making progress towards the base case?)
* For a binary string of length *n*, how many recursive calls will you do?


