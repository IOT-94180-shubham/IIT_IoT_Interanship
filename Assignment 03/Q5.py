#Default Parameter Values
def greet(name,message="What are you doing"):
    print(message,name)
    greet("Shuham")
    greet("Shubham","Good morning")

#Keyword Arguments
def student_info(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)

student_info(age=22, name="Shubham", course="Python")

#Passing a Function to Another Function
def sub(a, b):
    return a - b

def operate(func, x, y):
    return func(x, y)

result = operate(sub, 11110000,1008990)
print("Result:", result)
