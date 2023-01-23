def find_max_jobs(jobs):
    jobs.sort(key=lambda x: x[1])
    n = len(jobs)
    last_end_time = 0
    total_profit = 0
    selected_jobs = []
    for i in range(n):
        if jobs[i][0] >= last_end_time:
            last_end_time = jobs[i][1]
            total_profit += jobs[i][2]
            selected_jobs.append(jobs[i])
    total_jobs = len(jobs)
    total_earnings = sum([j[2] for j in jobs])
    remaining_jobs = total_jobs - len(selected_jobs)
    remaining_earnings = total_earnings - total_profit
    return remaining_jobs,remaining_earnings

jobs = [[0900, 1030, 100], [1000, 1200, 500], [1100, 1200, 300]]
remaining_jobs,remaining_earnings = find_max_jobs(jobs)
print(remaining_jobs,remaining_earnings) # returns 1,300