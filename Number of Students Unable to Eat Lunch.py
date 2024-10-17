class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = [0, 0]
        for student in students:
            count[student] += 1

        for sandwich in range(len(sandwiches)):
            if count[sandwiches[sandwich]] == 0:
                return len(sandwiches) - sandwich
            count[sandwiches[sandwich]] -= 1

        return 0
