class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        q = deque(students)

        res = n

        for sand in sandwiches:
            count = 0
            while count < n and q[0] != sand:
                cur = q.popleft()
                q.append(cur)
                count += 1
            
            if q[0] == sand:
                q.popleft()
                res -= 1
            else:
                break
        return res