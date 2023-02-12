mark=[]
print("Python progam to find Grades of Students")
c = 0

a = int(input("Enter number of subjects for which you want ot calculate marks"))

for i in range(a):
    print("Enter marks of Subject",i+1)
    mark.insert(i, int(input()))

for i in range(a):
    c = c + mark[i]

marks = c/a
print("Average Marks of Student:",marks)

if marks>85:
    print("Student has A grade")

elif marks>70:
    print("Student has B grade")
     
else:
    marks>60
    print("Student has C grade")