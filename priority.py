def priority_scheduling():
    n = int(input("Enter the number of processes: "))
    processes = []

    # Input process details
    for i in range(n):
        arrival = int(input(f"Enter arrival time for P{i + 1}: "))
        burst = int(input(f"Enter burst time for P{i + 1}: "))
        priority = int(input(f"Enter priority for P{i + 1} (lower number = higher priority): "))
        processes.append([i + 1, arrival, burst, priority])  # [PID, Arrival, Burst, Priority]

    # Sort by arrival time first, then by priority
    processes.sort(key=lambda x: (x[1], x[3]))

    # Initialize variables
    time, total_waiting_time, total_turnaround_time = 0, 0, 0
    completion_times = []

    print("\n{:<10}{:<15}{:<15}{:<15}{:<15}{:<15}".format(
        "Process", "Arrival Time", "Burst Time", "Priority", "Waiting Time", "Turnaround Time"
    ))

    # Process scheduling
    for pid, arrival, burst, priority in processes:
        if time < arrival:  # If CPU is idle
            time = arrival
        waiting_time = time - arrival
        turnaround_time = waiting_time + burst
        completion_time = time + burst
        total_waiting_time += waiting_time
        total_turnaround_time += turnaround_time
        time += burst
        completion_times.append(completion_time)

        # Print process details
        print("{:<10}{:<15}{:<15}{:<15}{:<15}{:<15}".format(
            f"P{pid}", arrival, burst, priority, waiting_time, turnaround_time
        ))

    # Print summary
    print(f"\nTotal Waiting Time: {total_waiting_time}")
    print(f"Average Waiting Time: {total_waiting_time / n:.2f}")
    print(f"Total Turnaround Time: {total_turnaround_time}")
    print(f"Average Turnaround Time: {total_turnaround_time / n:.2f}")

    # Print completion table
    print("\nCompletion Table")
    print("{:<10}{:<15}".format("Process", "Completion Time"))
    for i, pid in enumerate([p[0] for p in processes]):
        print("{:<10}{:<15}".format(f"P{pid}", completion_times[i]))


# Call the function
priority_scheduling()
