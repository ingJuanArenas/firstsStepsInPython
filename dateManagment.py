from datetime import datetime,date, time, timedelta
from operator import ne
from re import I
from time import strftime



print(datetime.now())
print("=========")
print(date.today())
print("==========")
print(date(2006,9,23))
print("==========")
datenow= datetime.now()
print(datenow.year)
print(datenow.month)
print(datenow.day)
print("======")
print(strftime("%A"))



today = date.today()
tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)
print(tomorrow, today, yesterday)


birthdat= date(2026,9,23)
print("======== ", birthdat - date.today())


timetomanipulate = datetime.now()
in5hours= timetomanipulate + timedelta(hours=5)
inless = timetomanipulate - timedelta(hours=8)
print(timetomanipulate)
print(in5hours)
print(inless)


for x in range(1,11):
    print(today + timedelta( days=x))

daterandom = "23/9/2006"
dateupdated = datetime.strptime(daterandom,"%d/%m/%Y")
print("=====================================")
print( dateupdated)
print(datetime.strftime(dateupdated, "%d/%m/%Y"))
print(datetime.strftime(dateupdated, "%m/%d/%Y"))
print(datetime.strftime(dateupdated, "%Y/%m/%d"))
print(datetime.strftime(dateupdated, "%A"))
print(datetime.strftime(dateupdated, "%A,%d de %B del %Y"))
print(datetime.strftime(dateupdated, "Today is, %A %d de %B of %Y"))

dates= list(["01/01/2024", "15/06/2024", "31/12/2024"])
for d in dates:
    new = datetime.strptime(d, "%d/%m/%Y")
    print(datetime.strftime(new, "%Y-%m-%d"))
# Corrección:
birth = input("Ingrese la fecha de nacimiento en formato DD/M/YYYY: ")
d = datetime.strptime(birth, '%d/%m/%Y') # Comillas añadidas
days_difference = (datetime.now() - d).days
years_difference = days_difference / 365.25 # Usar 365.25 para considerar años bisiestos
print(f"Han pasado aproximadamente {years_difference:.2f} años.")