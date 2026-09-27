class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        ordered_tasks = []

        for i, task in enumerate(tasks):
            ordered_tasks.append((task[0], task[1], i))
        
        ordered_tasks.sort(key = lambda x : x[0])

        res = []
        min_heap = []
        curr_time, task_idx = 0, 0
        n = len(tasks)

        while task_idx < n or min_heap:
            if not min_heap and curr_time < ordered_tasks[task_idx][0]:
                curr_time = ordered_tasks[task_idx][0]
            
            while task_idx < n and ordered_tasks[task_idx][0] <= curr_time:
                _, process_time, original_idx = ordered_tasks[task_idx]
                heapq.heappush(min_heap, (process_time, original_idx))
                task_idx += 1
            
            process_time, original_idx = heapq.heappop(min_heap)
            curr_time += process_time
            res.append(original_idx)
        return res