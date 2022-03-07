"""HackerRank - Nested lists
    Given the names and grades for each student in a class of students, 
store them in a nested list and print the name(s) of any student(s) having 
the second lowest grade.
https://www.hackerrank.com/challenges/nested-list/problem
"""
student_list = []
score_set = set()
for i in range(int(input('Enter the number of students'))):
    name = input('S{}-name: '.format(i+1))
    score = float(input('S{}-score: '.format(i+1)))
    student_list.append([name,score])
    score_set.add(score)
score_set = sorted(score_set)
s_2lg = [s[0] for s in student_list if s[1] == score_set[1]]
s_2lg = sorted(s_2lg)
print('The student(s) with second lowest grade are: ',end='')
for i in s_2lg:
    print(i,end=';')