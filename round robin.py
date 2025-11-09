def round_robin():
    n = int(input("Enter the number of processes: "))
    time_quantum = int(input("Enter time quantum: "))
    processes = []

    # Input process details
    for i in range(n):
        arrival = int(input(f"Enter arrival time for P{i + 1}: "))
        burst = int(input(f"Enter burst time for P{i + 1}: "))
        processes.append([i + 1, arrival, burst, burst, 0])  # [PID, Arrival, Burst, Remaining Burst, Completion Time]

    time, total_waiting_time, total_turnaround_time, completed = 0, 0, 0, 0
    ready_queue = []
    waiting_times = [0] * n
    turnaround_times = [0] * n
    completion_times = [0] * n

    print("\n{:<10}{:<15}{:<15}{:<15}{:<15}".format(
        "Process", "Arrival Time", "Burst Time", "Waiting Time", "Turnaround Time"
    ))

    # Process scheduling
    while completed < n:
        for p in processes:
            if p[1] <= time and p[3] > 0 and p not in ready_queue:
                ready_queue.append(p)

        if ready_queue:
            current_process = ready_queue.pop(0)
            pid, arrival, burst, remaining, _ = current_process

            if remaining > time_quantum:
                time += time_quantum
                current_process[3] -= time_quantum  # Reduce remaining burst time
            else:
                time += remaining
                current_process[3] = 0  # Process completed
                completed += 1
                completion_time = time
                turnaround_time = completion_time - arrival
                waiting_time = turnaround_time - burst

                # Update totals and process stats
                total_waiting_time += waiting_time
                total_turnaround_time += turnaround_time
                turnaround_times[pid - 1] = turnaround_time
                waiting_times[pid - 1] = waiting_time
                completion_times[pid - 1] = completion_time

                # Print process details
                print("{:<10}{:<15}{:<15}{:<15}{:<15}".format(
                    f"P{pid}", arrival, burst, waiting_time, turnaround_time
                ))
        else:
            time += 1  # If no process is ready, increment time

    # Summary
    print(f"\nTotal Waiting Time: {total_waiting_time}")
    print(f"Average Waiting Time: {total_waiting_time / n:.2f}")
    print(f"Total Turnaround Time: {total_turnaround_time}")
    print(f"Average Turnaround Time: {total_turnaround_time / n:.2f}")

    # Completion Table
    print("\nCompletion Table")
    print("{:<10}{:<15}".format("Process", "Completion Time"))
    for i, pid in enumerate([p[0] for p in processes]):
        print("{:<10}{:<15}".format(f"P{pid}", completion_times[i]))


# Call the function
round_robin()
