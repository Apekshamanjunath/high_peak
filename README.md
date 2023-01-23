# high_peak

/*For find the number of tasks and earnings available for others you can subtract the total number of tasks that Lokesh picked from the original number of tasks and subtract the total earnings of the tasks that Lokesh picked from the original total earning*/


/*Sample greedy approach methode python code to show the sheduling job*/


def find_max_jobs(jobs):
    jobs.sort(key=lambda x: x[1])
    n = len(jobs)
    last_end_time = 0
    total_profit = 0
    for i in range(n):
        if jobs[i][0] >= last_end_time:
            last_end_time = jobs[i][1]
            total_profit += jobs[i][2]
    return total_profit

jobs = [[0900, 1030, 100], [1000, 1200, 500], [1100, 1200, 300]]
profit = find_max_jobs(jobs)
print(profit) # returns 800


/*End of sample code for job scheduling*/




/*The common solution job shuduling in greedy algorithm the algorithm first sorts the jobs based on their end time and then iterates through the jobs, keeping track of the last end time and the total profit, if a job starts after the last end time, it is added to the schedule and the last end time is updated to the end time of this job. The algorithm continues until all jobs have been processed and then the process ends*/

/*Python program*/
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

