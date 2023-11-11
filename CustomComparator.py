import heapq


class MaxWrapper:
    def __init__(self, value) -> None:
        self.value = value

    def __lt__(self, obj) -> bool:
        return self.value > obj.value

    def __eq__(self, obj) -> bool:
        return self.value == obj.value

    def getValue(self) -> int:
        return self.value


class Student:
    def __init__(self, name: str, age: int, marks: int):
        self.name = name
        self.age = age
        self.marks = marks

    def print(self):
        print(self.name + " " + str(self.age) + " " + str(self.marks))

    def __lt__(self, obj) -> bool:
        if self.marks != obj.marks:
            return self.marks > obj.marks
        else:
            return self.age < obj.age

    def __eq__(self, __o: object) -> bool:
        return self.marks == __o.marks and self.age == __o.age


arr = [2, 1, 4, 3, 5]
# neg = [-1 * el for el in arr]
# heapq.heapify(neg)
# print("Max element is: " + str(-1 * heapq.heappop(neg)))
# wrapped_arr = [MaxWrapper(el) for el in arr]
# wrapped_arr = list(map(lambda item: MaxWrapper(item), arr))
# heapq.heapify(wrapped_arr)
# print("Max element is: " + str(heapq.heappop(wrapped_arr).getValue()))
students = []
students.append(Student("Abc", 19, 88))
students.append(Student("Soham", 24, 92))
students.append(Student("Xyz", 25, 92))
students.append(Student("Ghi", 21, 88))
heapq.heapify(students)
n = len(students)
for i in range(n):
    student = heapq.heappop(students)
    student.print()