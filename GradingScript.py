import string,csv

file1 = open("iClicker_EID_Score.csv","rb")
file2 = open("BlackBoard_EID_Q5.csv","rb")
file3 = open("out.csv","w")

reader1 = csv.reader(file1)
reader2 = csv.reader(file2)
writer = csv.writer(file3, delimiter = ',', quotechar='"', quoting = csv.QUOTE_ALL)
#writer = csv.writer(file3, delimiter = ',', quoting = csv.QUOTE_MINIMAL)


iClicker_EID_list = []
iClicker_Score_list = []

rownum = 0
for row in reader1:
    if rownum != 0:
        iClicker_EID_list.append(row[0])
        iClicker_Score_list.append(row[1])
    rownum += 1

print iClicker_EID_list
print iClicker_Score_list

dic = dict()
for i in range(len(iClicker_EID_list)):
    dic[iClicker_EID_list[i]] = iClicker_Score_list[i]


BlackBoard_EID_list = []
BlackBoard_Score_list = []

BlackBoard_Lastname_list=[]
BlackBoard_Firstname_list=[]
BlackBoard_EID_list=[]
BlackBoard_Quiz_list=[]
BlackBoard_lastaccess_list=[]

rownum = 0
for row in reader2:
    if rownum == 0:
        BlackBoard_header = row
        print row[0]
        print row
    else:
        BlackBoard_Lastname_list.append(row[0])
        BlackBoard_Firstname_list.append(row[1])
        BlackBoard_EID_list.append(row[2])
        BlackBoard_lastaccess_list.append(row[3])
        BlackBoard_Quiz_list.append(row[4])
    rownum += 1


writer.writerow(["Last Name"]+[BlackBoard_header[1]]+[BlackBoard_header[2]]+[BlackBoard_header[3]]+[BlackBoard_header[4]])

for i in range(len(BlackBoard_EID_list)):
    if BlackBoard_EID_list[i] in iClicker_EID_list:
        writer.writerow([BlackBoard_Lastname_list[i]]+[BlackBoard_Firstname_list[i]]+[BlackBoard_EID_list[i]]+[BlackBoard_lastaccess_list[i]]+[dic[BlackBoard_EID_list[i]]])
    else:
        writer.writerow([BlackBoard_Lastname_list[i]]+[BlackBoard_Firstname_list[i]]+[BlackBoard_EID_list[i]]+[BlackBoard_lastaccess_list[i]]+[BlackBoard_Quiz_list[i]])
 



"""

for i in StudentList:
    if i in iClicker_EID_list:
        print dic[i]
        file3.write(str(dic[i])+"\n")
    else:
        print 0
        file3.write(str(0)+"\n")
"""

file1.close()
file2.close()
file3.close()

