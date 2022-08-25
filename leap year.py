#To check whether entered year is leap or not
year= int(input("Enter year"))
leap= year%4
if leap==0:print("Entered year is leap")
else: print("Entered year is not leap")
