def worst_fit(block_sizes, process_sizes):
    allocation = [-1] * len(process_sizes)  # To store the allocation result
    
    for i, process in enumerate(process_sizes):
        worst_index = -1  # Initialize the worst index
        for j, block in enumerate(block_sizes):
            if block >= process:  # Check if block can fit the process
                # Find the block with the most space left after allocation
                if worst_index == -1 or block > block_sizes[worst_index]:
                    worst_index = j
        
        if worst_index != -1:
            allocation[i] = worst_index
            block_sizes[worst_index] -= process  # Update the block size after allocation
    
    return allocation

# User Input
block_sizes = list(map(int, input("Enter block sizes separated by space: ").split()))
process_sizes = list(map(int, input("Enter process sizes separated by space: ").split()))
allocation = worst_fit(block_sizes, process_sizes)

print("\nProcess Allocation:")
for i, block in enumerate(allocation):
    print(f"Process {i + 1} -> Block {block + 1 if block != -1 else 'Not Allocated'}")
