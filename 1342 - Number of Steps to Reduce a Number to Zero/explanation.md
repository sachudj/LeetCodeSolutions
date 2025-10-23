## Approach:

The solution uses a simulation-based approach to count the steps required to reduce the number to zero. Here's the breakdown:

1. Initialization: Start with `steps = 0` to track the number of operations.
2. Loop Until Zero: While `num > 0`:
    - Even Check: If `num` is even `(num % 2 == 0)`, divide by 2 (`num /= 2`).
    - Odd Check: If `num` is odd, subtract 1 (`num -= 1`).
    - Increment Steps: Each operation (division or subtraction) counts as one step.
3. Termination: Once `num` becomes `0`, return the total steps.
