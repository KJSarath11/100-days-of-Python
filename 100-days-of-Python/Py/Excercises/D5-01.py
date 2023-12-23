#average height
students_height=input().split()
for n in range(0,len(students_height)):
    students_height[n]=int(students_height[n])

total_height=0
for height in students_height:
    total_height+=height
print(f"Total height:{total_height}")

no_of_students=0
for no_of in students_height:
    no_of_students+=1
print(f"No fo students:{no_of_students}")

average=round(total_height/no_of_students)
print("Average Height:",average)

#printing max_height
max_height=0
for height in students_height:
    if height>max_height:
        max_height=height
print(f"max height:{max_height}")