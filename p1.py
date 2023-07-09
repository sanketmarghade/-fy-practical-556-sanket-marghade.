import pandas as pd
import csv
f1=open("D://556 a1\\stud_info.csv","r")





info_dataset=[]
while True:
    data=f1.readline()
    if data:
        info_dataset.append(data.replace("\n","").split(","))
    else:
        break;





RollNo=[]
name=[]
Gender=[]
DOB=[]
for row in info_dataset[1:]:
    RollNo.append(row[0])
    name.append(row[1])
    Gender.append(row[2])
    DOB.append(row[3])





f2=open("D://556 a1\\stud_placement.csv","r")




placement_dataset=[]
while True:
    data=f2.readline()
    if data:
        placement_dataset.append(data.replace("\n","").split(","))
    else:
        break;




RollNo=[]
Company=[]
JobRole=[]
Package=[]
for row in placement_dataset[1:]:
    RollNo.append(row[0])
    Company.append(row[1])
    JobRole.append(row[2])
    Package.append(row[3])




f3=open("D://556 a1\\student_marks.csv","r")



marks_dataset=[]
while True:
    data=f3.readline()
    if data:
        marks_dataset.append(data.replace("\n","").split(","))
    else:
        break;






Roll=[]
Maths=[]
Physics=[]
Chemistry=[]
Total=[]
Percentage=[]
for row in marks_dataset[1:]:
    Roll.append(row[0])
    Maths.append(row[1])
    Physics.append(row[2])
    Chemistry.append(row[3])
    Total.append(row[4])
    Percentage.append(row[5])






studentdata=[]
studentdata.append(Roll)
studentdata.append(name)
studentdata.append(Gender)
studentdata.append(DOB)
studentdata.append(Maths)
studentdata.append(Physics)
studentdata.append(Chemistry)
studentdata.append(Total)
studentdata.append(Percentage)
studentdata.append(Company)
studentdata.append(JobRole)
studentdata.append(Package)




student_details=[]
for i in range(len(marks_dataset)):
    student_details.append(info_dataset[i]+marks_dataset[i]+placement_dataset[i])







fw = open("D:/556 a1\\empty.csv", "w")
for row in student_details:
    w=csv.writer(fw)
    w.writerow(row)
fw.close()

f1=pd.read_csv(r"D:/556 a1\\empty.csv")
print(f1)
i=0

    
    
    
    
Maths_sum1=f1["Maths"].sum()
Physics_sum1=f1["Physics"].sum()
Chemistry_sum1=f1["Chemistry"].sum()

Maths_max1=f1["Maths"].max()
Physics_max1=f1["Physics"].max()
Chemistry_max1=f1["Chemistry"].max()

Maths_min1=f1["Maths"].min()
Physics_min1=f1["Physics"].min()
Chemistry_min1=f1["Chemistry"].min()

Maths_count1=f1["Maths"].count()
Physics_count1=f1["Physics"].count()
Chemistry_count1=f1["Chemistry"].count()

Maths_ave1=f1["Maths"].mean()
Physics_ave1=f1["Physics"].mean()
Chemistry_ave1=f1["Chemistry"].mean()



print("sum of maths",Maths_sum1)
print("sum of physics",Physics_sum1)
print("sum of chemistory",Chemistry_sum1)
print("max of math",Maths_max1)
print("max of physics",Physics_max1)
print("max of chemistry",Chemistry_max1)
print("min of maths",Maths_min1)
print("min of physics",Physics_min1)
print("min of chemistry",Chemistry_min1)
print("count of maths",Maths_count1)
print("count of physics",Physics_count1)
print("count of maths",Chemistry_count1)
print("average of maths",Maths_ave1)
print("average of physics",Physics_ave1)
print("average of chemistory",Chemistry_ave1)




               



    
    










