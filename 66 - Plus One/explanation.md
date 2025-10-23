## Approach:

1. Convert Digits to String: Combine the list of digits into a single string (e.g., `[1, 2, 3]` → `"123"`).
2. Convert to Integer: Parse the string into a numeric integer (e.g., `"123"` → `123`).
3. Increment by 1: Add `1` to the integer (e.g., `123 + 1 = 124`).
4. Convert Back to Digits: Split the resulting integer back into individual digits (e.g., `124` → `["1", "2", "4"]`), then convert each to an integer.

## Code Explanation

- `map(str, digits)`: Converts each digit to a string.
- `''.join(...)`: Combines the strings into a single number string.
- `int(...) + 1`: Increments the number.
- `str(...)`: Converts the incremented number back to a string.
- `[int(d) for d in ...]`: Splits the string into individual digits and converts them to integers.
