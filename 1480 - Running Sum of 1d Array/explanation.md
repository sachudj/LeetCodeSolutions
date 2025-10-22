## Approach:

1. Initialize an empty result list and a running sum variable
2. Iterate through each number in the input array:
    - Add the current number to the running sum
    - Append the updated sum to the result list
3. Return the result list containing cumulative sums

#### Example Walkthrough:

For `[3,1,2,10,1]`:
- Start with sum=0
- 3 → sum=3 → [3]
- 1 → sum=4 → [3,4]
- 2 → sum=6 → [3,4,6]
- 10 → sum=16 → [3,4,6,16]
- 1 → sum=17 → [3,4,6,16,17]

This solution has O(n) time complexity (n = array length) and O(n) space complexity, efficiently handling all valid inputs within constraints.
