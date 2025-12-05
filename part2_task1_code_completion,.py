import time
import random
import copy

# ==========================================
# Part 2, Task 1: AI-Powered Code Completion
# ==========================================

# Dataset Generation
def generate_data(size=1000):
    return [{'id': i, 'value': random.randint(1, 10000)} for i in range(size)]

data_manual = generate_data(5000)
data_ai = copy.deepcopy(data_manual)

# ---------------------------------------------------------
# 1. Manual Implementation (Simulating a naive approach)
# ---------------------------------------------------------
# Description: A developer might manually implement a sorting algorithm 
# like Bubble Sort if they forget about Python's built-in capabilities.

def manual_sort(data, key):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j][key] > data[j+1][key]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

print("Starting Manual Sort (Bubble Sort)...")
start_time = time.time()
manual_sort(data_manual, 'value')
end_time = time.time()
manual_duration = end_time - start_time
print(f"Manual Sort Time: {manual_duration:.6f} seconds")


# ---------------------------------------------------------
# 2. AI-Suggested Implementation (Optimized)
# ---------------------------------------------------------
# Description: AI tools (Copilot/ChatGPT) typically suggest using 
# Python's built-in `sorted()` or `.sort()` with a lambda key, 
# which uses Timsort (O(n log n)).

def ai_suggested_sort(data, key):
    return sorted(data, key=lambda x: x[key])

print("\nStarting AI-Suggested Sort (Timsort)...")
start_time = time.time()
ai_suggested_sort(data_ai, 'value')
end_time = time.time()
ai_duration = end_time - start_time
print(f"AI Sort Time: {ai_duration:.6f} seconds")


# ---------------------------------------------------------
# 3. Analysis & Comparison
# ---------------------------------------------------------
"""
ANALYSIS REPORT

1. Efficiency Comparison:
   - Manual Implementation (Bubble Sort): The time complexity is O(n^2). For a list of 5,000 items, this requires approx 25 million comparisons.
   - AI-Suggested Implementation (Timsort): Python's built-in sort is O(n log n). For 5,000 items, this is significantly faster.
   
   Observed Results:
   - Manual Sort took approx {manual_duration:.4f} seconds.
   - AI Sort took approx {ai_duration:.4f} seconds.
   - The AI suggestion is orders of magnitude faster.

2. Code Quality:
   - Manual: Verbose (7 lines), harder to read, and prone to off-by-one errors.
   - AI-Suggested: Concise (1 line), readable, and leverages highly optimized C-based internal libraries.

3. Conclusion:
   AI tools effectively guide developers toward "Pythonic" best practices, preventing the reinvention of the wheel with less efficient algorithms.
"""
print("\nAnalysis complete. See source code comments for details.")
