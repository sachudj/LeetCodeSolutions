## Approach:

1. Sort the array to enable the two-pointer approach.
2. Initialize a variable `closest_sum` to store the closest sum found (start with the sum of the first three elements).
3. Iterate through the array with a fixed element at index `i` (from `0` to `n-3`):
    - Set `left = i + 1` and `right = n - 1`.
    - While `left < right`:
        - Calculate `current_sum = nums[i] + nums[left] + nums[right]`.
        - If `current_sum == target`, return it immediately (exact match).
        - Update `closest_sum` if `abs(current_sum - target)` is smaller than the current closest difference.
        - If `current_sum < target`, increment `left` to increase the sum.
        - If `current_sum > target`, decrement `right` to decrease the sum.
4. Return closest_sum after processing all valid triplets.


Time Complexity: O(n²) due to sorting (O(n log n)) and nested loops (O(n²)).
Space Complexity: O(1) (no extra space used beyond input).