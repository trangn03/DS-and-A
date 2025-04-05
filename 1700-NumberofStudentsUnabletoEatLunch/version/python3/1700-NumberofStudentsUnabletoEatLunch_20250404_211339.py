# Last updated: 4/4/2025, 9:13:39 PM
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = students[:]
        stack = sandwiches[:]

        while queue and stack:
            student = queue[0]
            sandwich = stack[0]

            if student == sandwich:
                queue.pop(0) # Student takes sandwich and leave
                stack.pop(0) # Sandwich removes
            else:
                # No student can each
                if sandwich not in queue:
                    break
                queue.append(queue.pop(0)) # Student goes to the end of the queue
        return len(queue)
        