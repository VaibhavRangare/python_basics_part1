# For String both ' and " works
course = 'Python'                               # using ingle quotes
name = 'Vaibhav'
print(course)
course_new = "Python"                           # using double quotes
# course_mid_term = 'Python's course            # will not work
course_mid_term = "Python's Course"
print(course_mid_term)                          # Python's Course
course_mid_term = 'Python "Full course"'
print(course_mid_term)                          # Python "Full course"
multiple_line = '''                             
this is multiple line 
text message
'''
print(multiple_line)
multiple_line = """ 
this is multiple line 
text message
"""
print(multiple_line)
course = 'Python'
print(course[0])                                # P, first char of course
print(course[-1])                               # n, last char of course
print(course[-2])                               # o , second last char of course
# Python
# 012345
print(course[0:3])                              # Pyt, known as slicing, one character less than the index
# course[:] == course[0:length of the string]
# Formatted string
msg = f'{course} is assigned to {name}'
print(msg)
print(len(course))                              # length of String is 6
