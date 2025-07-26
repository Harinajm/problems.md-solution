# problems.md-solution
Programming Challenges - Agetware Assignment
This repository contains the solutions for the Programming Challenges (problems.md) part of the Agetware technical assignment. It features efficient and well-documented Python solutions for four distinct problems.

1. How to Run the Solutions
Prerequisites
Python 3

Step 1: Clone the Repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

Step 2: Run the Code
All solutions are contained within the solutions.py file. You can run this file directly from your terminal to see the output from the example test cases.

python solutions.py

2. Problem Solutions
This section details the approach and implementation for each of the four problems.

Problem 1: Caesar Cipher
a. Problem Statement
Implement the Caesar cipher, a simple substitution cipher where each letter in a message is shifted by a fixed number of positions down the alphabet. The function must support both encoding and decoding.

b. Algorithm and Design
The solution is a single, versatile function caesar_cipher. It iterates through the input string, applying the shift only to alphabetic characters while preserving their original case. Non-alphabetic characters are ignored. The core of the logic uses modular arithmetic (% 26) to ensure the alphabet wraps around correctly. To handle both encoding and decoding efficiently, the shift value is simply negated when the function is in 'decode' mode.
Problem 2: Indian Currency Format
a. Problem Statement
Develop a function that takes a floating-point number and converts it into the Indian currency string format, which groups the last three digits and then groups the remaining digits in pairs (e.g., 12,34,567).

b. Algorithm and Design
The function format_indian_currency first separates the integer and fractional parts of the number. The integer part is then formatted: if its length is greater than three, the last three digits are handled separately. The remaining digits are then iterated through from right to left, inserting a comma every two characters. The final result is a concatenation of the formatted integer part and the original fractional part.
Problem 3: Combining Two Lists
a. Problem Statement
Given two sorted lists of elements, where each element has a position and values, combine them. A combination occurs if more than half of one element's length is contained within the other. The new element takes the position of the one that appears first.

b. Algorithm and Design
An efficient two-pointer approach is used to traverse both lists in a single pass (O(n+m) time complexity). At each step, the overlap between the two current elements is calculated. If the overlap satisfies the "more than half" condition, the elements are merged. Otherwise, the element that appears earlier in the sequence is added to the result, and its corresponding pointer is advanced.
Problem 4: Minimizing Loss
a. Problem Statement
Given a list of house prices over several years, find the minimum loss incurred by buying in one year and selling in a subsequent year. The output must include the buy year, sell year, and the loss amount.

b. Algorithm and Design
The solution has an O(n log n) time complexity. It begins by pairing each price with its original year. This list is then sorted by price. By iterating through the sorted list, we can efficiently check adjacent price pairs. A transaction is valid only if the buy year (associated with the higher price) occurred before the sell year (associated with the lower price). The algorithm tracks the minimum valid loss found during this single pass.
