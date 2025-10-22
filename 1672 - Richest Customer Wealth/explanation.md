## Approach:

1. For each customer (each row in the `accounts` matrix), calculate their total wealth by summing all their bank balances
2. Use Python's `max()` function to find the highest total wealth among all customers

#### Example Walkthrough:

- For accounts = `[[1,5],[7,3],[3,5]]`:
  - Customer 1: 1+5 = 6
  - Customer 2: 7+3 = 10
  - Customer 3: 3+5 = 8
  - Maximum wealth = 10


This solution has O(m*n) time complexity (m = number of customers, n = number of banks) and O(1) space complexity, efficiently handling all constraints. The one-liner approach leverages Python's built-in functions for concise and readable code.
