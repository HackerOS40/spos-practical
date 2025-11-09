def best_fit(block_sizes, process_sizes):
    allocation = [-1] * len(process_sizes)
    
    print(f"\nMemory Blocks Before Allocation: {block_sizes}")
    
    for i, process in enumerate(process_sizes):
        best_index = -1
        for j, block in enumerate(block_sizes):
            # Check if the block can accommodate the process
            if block >= process:
                if best_index == -1 or block < block_sizes[best_index]:
                    best_index = j
        
        if best_index != -1:
            allocation[i] = best_index
            block_sizes[best_index] -= process
            print(f"Process of size {process} allocated to block {best_index + 1} (Best Fit)")
        else:
            print(f"No suitable block found for process of size {process} (Best Fit)")
    
    return allocation

# User Input
block_sizes = list(map(int, input("Enter block sizes separated by space: ").split()))
process_sizes = list(map(int, input("Enter process sizes separated by space: ").split()))

# Perform Best Fit Allocation
allocation = best_fit(block_sizes, process_sizes)
