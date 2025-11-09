def first_fit(block_sizes, process_sizes):
    allocation = [-1] * len(process_sizes)
    
    print(f"\nMemory Blocks Before Allocation: {block_sizes}")

    # Iterate through each process
    for i, process in enumerate(process_sizes):
        allocated = False
        for j, block in enumerate(block_sizes):
            # Find the first block that fits the process
            if block >= process:
                allocation[i] = j
                block_sizes[j] -= process  # Reduce block size after allocation
                print(f"Process of size {process} allocated to block {j + 1} (First Fit)")
                allocated = True
                break

        # If no suitable block is found
        if not allocated:
            print(f"No suitable block found for process of size {process} (First Fit)")

    return allocation

# User Input
block_sizes = list(map(int, input("Enter block sizes separated by space: ").split()))
process_sizes = list(map(int, input("Enter process sizes separated by space: ").split()))

# Perform First Fit Allocation
allocation = first_fit(block_sizes, process_sizes)

# Output final allocation
print("\nProcess Allocation:")
for i, block in enumerate(allocation):
    print(f"Process {i + 1} -> Block {block + 1 if block != -1 else 'Not Allocated'}")
