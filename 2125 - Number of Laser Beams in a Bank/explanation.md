### 🔍 **Problem Understanding**

We are given a binary string array `bank`, where:

*   Each string represents a row in the bank.
*   `'1'` = security device
*   `'0'` = empty cell

A **laser beam** exists between two devices if:

1.  They are on **different rows** (r1 < r2).
2.  All rows **between** r1 and r2 have **no devices** (i.e., all zeros).

> So, beams only go from one row with devices to the next **non-empty** row below it (skipping any empty rows in between).

- - -

### ✅ **Key Insight**

Instead of checking every pair of devices (which would be O(n²)), we can observe:

*   Only **adjacent non-empty rows** contribute to beams.
*   If row `i` has `a` devices and the next non-empty row `j` has `b` devices, then total beams between them = `a * b`.
*   We can iterate through rows, count devices per row, and multiply counts of consecutive non-empty rows.

- - -

### 🧠 **Approach**

1.  Traverse each row.
2.  Count the number of `'1'`s in the current row.
3.  Keep track of the previous non-zero row’s device count.
4.  If current row has devices, add `(prev_count * curr_count)` to result.
5.  Update `prev_count = curr_count`.

> This avoids nested loops and runs in **O(m × n)** time.

- - -

### 📌 Example Walkthrough

```python
bank = ["011001", "000000", "010100", "001000"]
```

Apply Code

*   Row 0: `'011001'` → 3 devices → `prev_devices = 3`
*   Row 1: `'000000'` → 0 devices → skip
*   Row 2: `'010100'` → 2 devices → add `3 * 2 = 6`, update `prev_devices = 2`
*   Row 3: `'001000'` → 1 device → add `2 * 1 = 2`, update `prev_devices = 1`

Total = `6 + 2 = 8` ✅

- - -

### ⏱️ Time Complexity: O(m × n)

### 🧠 Space Complexity: O(1)