#Q1

print('enter the year')
year = int(input())
if ((year % 400 == 0) or (( year%4 == 0) and (year%100 !=0))):
    print('%d IS leap year'%year)
else:
    print('%d IS NOT a leap year' %year)

#Q2

print('\n')
print('enter the 2 sides of the parallelogram')
side1 = int(input())
side2 = int(input())
if side1 == side2 :
    print('the parallelogram with side %d is a SQUARE'%side1)
else:
    print('the parallelogram with sides %d & %d is a RECTANGLE' %(side1,side2))

#Q3

print('\n')
print('enter the age of the 3 people')
a1 = int(input())
a2 = int(input())
a3 = int(input())
if a1 >= a2 and a1 >= a3:
    old = a1
elif a2 >= a1 and a2 >= a3:
    old = a2
else:
    old = a3
if a1 <= a2 and a1 <= a3:
    young = a1
elif a2 <= a1 and a2 <= a3:
    young = a2
else:
    young = a3
print('the person with age %d is oldest', old)
print('ehe person with age %d is youngest', young)

#Q4

print('\n')
print("enter applicant's age, sex(m/f), and marital status(y/n)")
age1 = int(input())
sex = input()
ms = input()
if (sex == 'f' or sex == 'F'):
    print('Applicant is eligible only to work in URBAN AREA')
elif (sex == 'm' or sex == 'M'):
    if 20 <= age1 < 40:
        print("As applicant's age is %d, he can work ANYWHERE" % age1)
    elif 40 <= age1 < 60:
        print("As applicant's age is %d, he can work in URBAN AREAS only" % age1)
else:
    print('Error')

#Q5

print ("Enter quantity")
quantity = int(input())
if quantity > 1000:
  print ("Cost is",((quantity*100)-(.1*quantity*100)))
else:
  print ("Cost is",quantity*100)
				

# LOOPS

#Q1

print('\n')
n = []
print('enter 10 numbers')
for i in range(10):
    a = int(input())
    n.append(a)
for i in range(10):
    print('no: ', n[i])

#Q2

print('\n')
while True:
 print('infinite')


#Q3

print('\n')
n = int(input("Enter the number of elements\n"))
print("Enter the elements")
l1 = []
for i in range(n):
    a = int(input())
    l1.append(a)
l2 = []
j = int(input())
while j != 0:
    l1.append(j)
    j = int(input())
for j in range(n):
    a = int(l1[j] * l1[j])
    l2.append(a)
print(l1)
print(l2)

#Q4

print('\n')
print('enter the list elements')
l1 = []
lint = []
lflt = []
lstr = []
i = 'a'
while str(i) != '-1':
    i = input()
    l1.append(i)
    print("to end entering in list enter '-1' otherwise enter next element")
    i = input()
for i in range(len(l1)):
    if l1[i].isalpha():
        lstr.append(l1[i])
    elif l1[i].isdecimal():
        lflt.append(l1[i])
    elif l1[i].isnumeric():
        lint.append(l1[i])
print('original list: ', l1)
print('int list: ', lint)
print('float list: ', lflt)
print('string list: ', lstr)

#Q5

print('\n')
l1 = []
for i in range(1, 101):
    flag = True
    for j in range(2, int(i/2)+1):
        if i % j == 0:
            flag = False
            continue
    if flag:
        l1.append(i)
print(l1)

#Q6

print('\n')
for i in range(1, 5):
    print('*' * i)

#Q7
    
print('\n')
print('enter the list elements and type "end" for ending input of list 1')
l1 = []
i = input()
while i != 'end':
    l1.append(i)
    i = input()
test = input('enter the element you want to search\n')
count = len(l1)
for i in range(0, count):
    if l1[i] == test:
        del l1[i]
        count -= 1
print(l1)
