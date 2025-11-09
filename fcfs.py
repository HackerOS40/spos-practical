def calculate_fcfs(processes, arrival_times, burst_times):
    n = len(processes)
    waiting_times = [0] * n
    turnaround_times = [0] * n
    completion_times = [0] * n

    # Calculate completion, turnaround, and waiting times
    for i in range(n):
        if i == 0:
            completion_times[i] = arrival_times[i] + burst_times[i]
        else:
            completion_times[i] = max(arrival_times[i], completion_times[i - 1]) + burst_times[i]

        turnaround_times[i] = completion_times[i] - arrival_times[i]
        waiting_times[i] = turnaround_times[i] - burst_times[i]

    return waiting_times, turnaround_times, completion_times

def print_schedule(processes, arrival_times, burst_times, waiting_times, turnaround_times, completion_times):
    # Print header with alignment
    print("\n{:<10}{:<15}{:<15}{:<20}{:<15}{:<15}".format(
        "Process", "Arrival Time", "Burst Time", "Completion Time", "Waiting Time", "Turnaround Time"))
    
    # Print each row with aligned columns
    for i in range(len(processes)):
        print("{:<10}{:<15}{:<15}{:<20}{:<15}{:<15}".format(
            processes[i], arrival_times[i], burst_times[i], completion_times[i], waiting_times[i], turnaround_times[i]))

def main():
    print("First-Come, First-Served (FCFS) CPU Scheduling Simulation")
    
    n = int(input("Enter the number of processes: "))
    processes = []
    arrival_times = []
    burst_times = []

    for i in range(n):
        process_name = f"P{i+1}"
        processes.append(process_name)
        arrival_time = int(input(f"Enter arrival time for {process_name}: "))
        burst_time = int(input(f"Enter burst time for {process_name}: "))
        arrival_times.append(arrival_time)
        burst_times.append(burst_time)

    # Sort processes based on arrival times
    sorted_processes = sorted(zip(processes, arrival_times, burst_times), key=lambda x: x[1])
    processes, arrival_times, burst_times = zip(*sorted_processes)

    # Calculate waiting times, turnaround times, and completion times
    waiting_times, turnaround_times, completion_times = calculate_fcfs(processes, arrival_times, burst_times)

    # Print the schedule
    print_schedule(processes, arrival_times, burst_times, waiting_times, turnaround_times, completion_times)

    # Print total waiting time and average turnaround time
    total_waiting_time = sum(waiting_times)
    total_turnaround_time = sum(turnaround_times)
    average_waiting_time = total_waiting_time / n
    average_turnaround_time = total_turnaround_time / n

    print(f"\nTotal Waiting Time: {total_waiting_time}")
    print(f"Average Waiting Time: {average_waiting_time:.2f}")
    print(f"Total Turnaround Time: {total_turnaround_time}")
    print(f"Average Turnaround Time: {average_turnaround_time:.2f}")

if __name__ == "__main__":
    main()
