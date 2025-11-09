def sjf_preemptive():
    n = int(input("Enter the number of processes: "))
    processes = []

    for i in range(n):
        arrival = int(input(f"Enter arrival time for P{i + 1}: "))
        burst = int(input(f"Enter burst time for P{i + 1}: "))
        processes.append([i + 1, arrival, burst, burst, 0, 0])  # [PID, Arrival Time, Burst Time, Remaining Time, Completion Flag, Completion Time]

    time, total_waiting_time, total_turnaround_time = 0, 0, 0
    completed, ready_queue = 0, []

    print("\nProcess Completion Table (Completion Time for Each Process):")
    print("PID    Arrival Time    Burst Time    Completion Time")

    while completed < n:
        # Add all arriving processes to the ready queue
        for p in processes:
            if p[1] <= time and p[4] == 0 and p not in ready_queue:
                ready_queue.append(p)

        if ready_queue:
            # Sort ready queue by remaining burst time to implement preemption
            ready_queue.sort(key=lambda x: x[3])
            current_process = ready_queue[0]
            pid, arrival, burst, remaining, completed_flag, completion_time = current_process

            # Process current process for one unit time
            time += 1
            current_process[3] -= 1  # Reduce remaining time by 1

            if current_process[3] == 0:  # If process is complete
                ready_queue.pop(0)  # Remove from queue
                current_process[4] = 1  # Mark as completed
                current_process[5] = time  # Record completion time
                completed += 1
                print(f"P{pid}    {arrival}             {burst}             {time}")
        else:
            time += 1  # Increment time if no process is ready to run

    print("\nDetailed Scheduling Analysis:")
    print("Process Arrival Time    Burst Time      Waiting Time    Turnaround Time")
    for pid, arrival, burst, _, _, completion_time in processes:
        turnaround_time = completion_time - arrival
        waiting_time = turnaround_time - burst
        total_waiting_time += waiting_time
        total_turnaround_time += turnaround_time
        print(f"P{pid}      {arrival}               {burst}               {waiting_time}               {turnaround_time}")

    print(f"\nTotal Waiting Time: {total_waiting_time}")
    print(f"Average Waiting Time: {total_waiting_time / n:.2f}")
    print(f"Total Turnaround Time: {total_turnaround_time}")
    print(f"Average Turnaround Time: {total_turnaround_time / n:.2f}")

# Run the function
sjf_preemptive()
