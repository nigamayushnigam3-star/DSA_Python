# DSA Python 🐍

A collection of **Data Structures and Algorithms problems implemented in Python**.

This repository contains my DSA practice for **coding interviews and problem-solving**, including LeetCode problems and fundamental data-structure implementations.

---

## 📚 Topics Covered

* Arrays
* Linked Lists
* Two Pointers
* Recursion
* Divide and Conquer
* Dynamic Programming
* Binary Search

---

## 🧩 Data Structures

| Data Structure     | Description                         |
| ------------------ | ----------------------------------- |
| Singly Linked List | Insertion, deletion and traversal   |
| Doubly Linked List | Basic implementation and operations |
| Stack              | Stack implementation and operations |

---

## 💻 LeetCode Problems

### 🔗 Linked List

| Problem                                                                                                                                            | Solution |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| [0019 - Remove Nth Node From End of List](https://github.com/nigamayushnigam3-star/DSA_Python/tree/main/0019-remove-nth-node-from-end-of-list)     | Python   |
| [0021 - Merge Two Sorted Lists](https://github.com/nigamayushnigam3-star/DSA_Python/tree/main/0021-merge-two-sorted-lists)                         | Python   |
| [0083 - Remove Duplicates from Sorted List](https://github.com/nigamayushnigam3-star/DSA_Python/tree/main/0083-remove-duplicates-from-sorted-list) | Python   |
| [0203 - Remove Linked List Elements](https://github.com/nigamayushnigam3-star/DSA_Python/tree/main/0203-remove-linked-list-elements)               | Python   |

### 📦 Array

| Problem                                                                                                                                      | Solution |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| [0053 - Maximum Subarray](https://github.com/nigamayushnigam3-star/DSA_Python/tree/main/0053-maximum-subarray)                               | Python   |
| [0121 - Best Time to Buy and Sell Stock](https://github.com/nigamayushnigam3-star/DSA_Python/tree/main/0121-best-time-to-buy-and-sell-stock) | Python   |
| [0704 - Binary Search](https://github.com/nigamayushnigam3-star/DSA_Python/tree/main/0704-binary-search)                                     | Python   |

### 👆 Two Pointers

| Problem                                                                                                                                        | Solution |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| [0019 - Remove Nth Node From End of List](https://github.com/nigamayushnigam3-star/DSA_Python/tree/main/0019-remove-nth-node-from-end-of-list) | Python   |

### 🔄 Recursion

| Problem                                                                                                                              | Solution |
| ------------------------------------------------------------------------------------------------------------------------------------ | -------- |
| [0021 - Merge Two Sorted Lists](https://github.com/nigamayushnigam3-star/DSA_Python/tree/main/0021-merge-two-sorted-lists)           | Python   |
| [0203 - Remove Linked List Elements](https://github.com/nigamayushnigam3-star/DSA_Python/tree/main/0203-remove-linked-list-elements) | Python   |

### 🧠 Divide and Conquer

| Problem                                                                                                        | Solution |
| -------------------------------------------------------------------------------------------------------------- | -------- |
| [0053 - Maximum Subarray](https://github.com/nigamayushnigam3-star/DSA_Python/tree/main/0053-maximum-subarray) | Python   |

### 📈 Dynamic Programming

| Problem                                                                                                                                      | Solution |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| [0053 - Maximum Subarray](https://github.com/nigamayushnigam3-star/DSA_Python/tree/main/0053-maximum-subarray)                               | Python   |
| [0121 - Best Time to Buy and Sell Stock](https://github.com/nigamayushnigam3-star/DSA_Python/tree/main/0121-best-time-to-buy-and-sell-stock) | Python   |

### 🔎 Binary Search

| Problem                                                                                                  | Solution | Time         | Space    |
| -------------------------------------------------------------------------------------------------------- | -------- | ------------ | -------- |
| [0704 - Binary Search](https://github.com/nigamayushnigam3-star/DSA_Python/tree/main/0704-binary-search) | Python   | **O(log n)** | **O(1)** |

---

## 🔍 Binary Search

Binary Search is an efficient searching algorithm used on a **sorted array**.

### Basic Approach

1. Set `low = 0`
2. Set `high = n - 1`
3. Find the middle element:

   ```python
   mid = (low + high) // 2
   ```
4. Compare `nums[mid]` with the target.
5. If the middle element is greater than the target, search the left half.
6. Otherwise, search the right half.
7. Continue until the target is found or the search space becomes empty.

### Python Implementation

```python
def binarySearch(nums, target):
    n = len(nums)

    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] > target:
            high = mid - 1

        else:
            low = mid + 1

    return -1
```

### Complexity

* **Best Case:** `O(1)`
* **Average Case:** `O(log n)`
* **Worst Case:** `O(log n)`
* **Space Complexity:** `O(1)` for iterative implementation

---

## ▶️ Running Python Examples

From the project root:

```bash
python LinkList/SLL.py
python DDL/ddl.py
```

No third-party Python packages are required.

---

## 🎯 Goal

The goal of this repository is to continuously practice DSA problems, improve problem-solving skills, and prepare for **technical interviews and placements**.

More problems and topics will be added regularly.

---

## 👨‍💻 Author

**Ayush Nigam**

GitHub: [@nigamayushnigam3-star](https://github.com/nigamayushnigam3-star)

---

⭐ If you find this repository useful, consider giving it a star!

<!---LeetCode Topics Start-->
# LeetCode Topics
## Array
|  |
| ------- |
| [0001-two-sum](https://github.com/nigamayushnigam3-star/DSA_Python/tree/master/0001-two-sum) |
## Hash Table
|  |
| ------- |
| [0001-two-sum](https://github.com/nigamayushnigam3-star/DSA_Python/tree/master/0001-two-sum) |
<!---LeetCode Topics End-->