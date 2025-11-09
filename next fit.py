def next_fit(block_sizes, process_sizes):
    allocation = [-1] * len(process_sizes)
    last_position = 0

    print("\nMemory Blocks Before Allocation:", block_sizes)

    for i, process in enumerate(process_sizes):
        for j in range(len(block_sizes)):
            index = (last_position + j) % len(block_sizes)  # Circular search
            if block_sizes[index] >= process:
                allocation[i] = index
                block_sizes[index] -= process
                last_position = index
                print(f"Process of size {process} allocated to block {index + 1} (Next Fit)")
                break
        else:
            print(f"No suitable block found for process of size {process} (Next Fit)")
    
    return allocation

# User Input
block_sizes = list(map(int, input("Enter block sizes separated by space: ").split()))
process_sizes = list(map(int, input("Enter process sizes separated by space: ").split()))

allocation = next_fit(block_sizes, process_sizes)

print("\nProcess Allocation:")
for i, block in enumerate(allocation):
    print(f"Process {i + 1} -> Block {block + 1 if block != -1 else 'Not Allocated'}")
