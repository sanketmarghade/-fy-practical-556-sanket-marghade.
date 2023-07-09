import csv
from collections import Counter
f1 = open("D:/556 a1/sales.csv","r")
product_details = [ ]
customer_details = [ ]
supplier_details = { }
supplist = [ ]
gender = [ ]
while(True): 
    data = f1.readline()
    if not data:
        break;
    #print(data)
    data = data.replace("\n","")
    # print(data)
    temp = data.split(",")
    print(temp)
    product_details.append(temp[1])
    customer_details.append(temp[3]) # type: ignore
    supplier_details.update({temp[1]:temp[2]})
    supplist.append(temp[2])
    gender.append(temp[4])
f1.close() 
customer_details = tuple(customer_details)
# print(supplist)
# print(supplier_details)
frequency = { }
for items in product_details: 
   if items in frequency: 
      frequency[items]+=1
   else: 
     frequency[items]=1
# print("\n\n\n")
# print(frequency.items())
# print("\n\n\n\n")
marklist = sorted(frequency.items(),key = lambda x: 
x[1],reverse = True)
# print(marklist)
# marklist= dict(marklist)
# print(marklist)
print(f"Most Poppular Item is : {marklist[0][0]}")
# print(supplier_details)
supplierList = list(supplier_details.items())
# print(supplierList)
CounterDict = Counter(supplist)
# print(CounterDict)
poplist = sorted(CounterDict.items(),key = lambda x : x[1], 
reverse = True)
poplist = list(poplist)
print(f"Best Supplier is: {poplist[0][0]}")
CountCustomer = Counter(customer_details)
# print(CountCustomer)
CustomerCountList = sorted(CountCustomer.items(),key =
lambda x: x[1], reverse = True)
CustomerCountList = list(CustomerCountList)
print(f"Customer Who Bought Most Products is:{CustomerCountList[0][0]}")
# print(gender)
countGender = Counter(gender)
# countGender = list(countGender)
a = (countGender.get("Female"))
print(f"No of Females are: {a}")