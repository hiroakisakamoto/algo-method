
# これもTLE
X = int(input())
Q = int(input())



completed_time = []

for _ in range(Q):
    query = list(map(int, input().split()))

    t = query[1]
    if query[0] == 0:
        completed_time.append(t+X)
    else:
        finished_tasks = []
        for time in completed_time:
            if time > t:
                break
            else:
                finished_tasks.append(time)
        print(len(finished_tasks))
        
        
        # finished_tasks = [x for x in completed_time if x <= t] 
        # print(len(finished_tasks))
