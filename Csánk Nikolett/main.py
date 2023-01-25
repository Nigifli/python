from os import system

normalPrice: int=None
choice: int=None
classStudents: int=None
groupDiscount: int=None
studentDiscount: int=None
schoolDiscount: int=None
worthestDeal: int=None
worthestPrice: int=None

print("Kérem adja meg nelyik helyszínen szeretne kirándulni!\n-Velencei tó (1)\n-Tihany és Balatonfüred (2)")
choice=int(input())

if (choice==1):
    normalPrice=6000
else:
    normalPrice=7500

print("Kérem adja meg a létszámot: ")
classStudents=int(input())
if(classStudents < 5):
    groupDiscount=normalPrice
elif(classStudents >= 5 and classStudents <=15):
    groupDiscount=normalPrice* 0.95
elif(classStudents >=15 and classStudents <= 25):
    groupDiscount=normalPrice* 0.92
else:
    groupDiscount=normalPrice* 0.85

if(classStudents < 5):
    schoolDiscount=normalPrice
elif(classStudents>=5 and classStudents<=10):
    schoolDiscount=normalPrice(classStudents-1)/classStudents
elif(classStudents >=11 and classStudents<=20):
    schoolDiscount=normalPrice*(classStudents-2)/classStudents
else:
    schoolDiscount=normalPrice*(classStudents-3)/classStudents

studentDiscount=normalPrice* 0.92

if(groupDiscount<classStudents and groupDiscount<studentDiscount):
    worthestDeal="Csoportos kedvezmény"
    worthestPrice=groupDiscount
elif(schoolDiscount<groupDiscount and schoolDiscount<studentDiscount):
    worthestDeal="Intézményi kedvezmény"
    worthestPrice=schoolDiscount
elif(schoolDiscount==groupDiscount):
    worthestDeal="Intézményi kedvezmény vagy csoportos kedvezmény"
    worthestPrice=schoolDiscount
elif(schoolDiscount==studentDiscount):
    worthestPrice=schoolDiscount
    worthestDeal="Intézményi kezdvezmény vagy diákkedvezmény"
elif(studentDiscount<groupDiscount and studentDiscount<schoolDiscount):
    worthestDeal="Diákkedvezmény"
    worthestPrice=studentDiscount
elif(groupDiscount==studentDiscount):
    worthestDeal="Csoportos kedvezmény vagy diákkedvezmény"
    worthestPrice=groupDiscount
else:
    worthestDeal="Diákkedvezmény"


print(f"Csoportkedvezményes ár: {groupDiscount}")
print(f"Intézményi kedvezményes ár: {schoolDiscount}")
print(f"Diákkedvezményes ár: {studentDiscount}")
print(f"A legjobb ajánlat a/az {worthestDeal}! {classStudents} fő esetén: {worthestPrice} Ft.")