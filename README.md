# Drome Problem

Problem belonging to the post-classroom Mock Interview Question Repository.

## Problem Statement

Given the head of a singly linked list, write a function is_palindrome that returns `True` if the list is a palindrome and `False` if it is not a palindrome.

For example:
5 → 4 → 2 is NOT a palindrome
5 → 4 → 5 is a palindrome

The list will be represented using the provided `Node` class.

It is guaranteed that the list will not have any cycles.

Adapted from: https://leetcode.com/problems/palindrome-linked-list/

## Examples

### Additional Palindrome Examples

5 → 4 → 5

a → b → c → c → b → a

3 → 3

5 _(only one element in list)_

_(empty list)_

### Additional Not-Palindrome Examples

5 → 4 → 2

a → b → c → E → b → a

## Notes for the Interviewer

### Clarifying Questions

#### Q: What should I do if the input is `None`?

A: Your code should treat a head of `None` as an empty list. We will consider an empty list to be a palindrome, so your code should return `True`.

#### Q: What should I do if the list has only a single element?

A: We will consider a single element list to be a palindrome, so your code should return `True`.

#### Q: Will the input contain any cycles?

A: No.

#### Q: What should I do if invalid input is passed in?

A: You can assume that the input will be valid.

#### Q: What data types will be stored in the values?

A: Any data types that can be checked for equality.

### Hints

- If your candidate struggles with an initial algorithm, encourage them to walk through an example and describe how they would do it using only pen and paper

- If the candidate still struggles to form an algorithm, ask them if there is a different data structure (other than a linked list) that would be easier for them to determine if it was a palindrome. Ask the candidate how they might write code that would convert the linked list into that data structure.

## Optional Bonus At-Home Challenges

To be attempted after completing the interview.

- The given solution is O(n)/O(n) time/space complexity where n is the number of nodes in the list. Can you come up with an O(n)/O(1) time/space complexity solution? It's a tricky one!
