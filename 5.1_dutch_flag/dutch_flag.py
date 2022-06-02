
def dutch_flag(A, pivot_idx):

    pivot = A[pivot_idx]
    start, end = 0, len(A)-1

    # First pass
    for i in range(len(A)):
        if A[i] < pivot:
            A[start], A[i] = A[i], A[start]
            start += 1
    # Second pass
    for i in range(len(A)-1, start-1, -1):
        if A[i] > pivot:
            A[end], A[i] = A[i], A[end]
            end -= 1

    return A

# Multiple correct answers for a single input, so just print out and check manually.
# This doesn't mean the algorithm produces outputs, but the problem stated has multiple correct answers.
print(dutch_flag([2,4,1,3,7,6,5], 4))
print(dutch_flag([1,2,2,2,3,3,2,2,1,1,2,2,1,2,1,3,1,2], 4))
