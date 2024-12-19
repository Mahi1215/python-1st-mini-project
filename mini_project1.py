print("THIS IS A SELECTION FOR SOFTWARE ENGINEERS!! THANK YOU")

print("INSTRUCTIONS:")
print("""THE QUALIFICATION MUST BE PROVIDED AS FOLLOWED:
      computer engineer
      artificial intelligence
      AI/ML""")

selected_emp=[]
rejected_emp=[]
name=input("enter the candidate name:")
age=int(input("enter the age of the candidate:"))
qual=input("enter the qualification of the candidate:")
exp=int(input("enter the minimum experience the candidate has(in years):"))

if age > 18 and qual in ["computer engineer","artificial intelligence","AI/ML",] and exp > 2:
    print(f"{name }Congratulations!! you have been selected")
    selected_emp.append(name)
else:
    print(f"Sorry!{name} you are not eligible for our job placement,BEST OF LUCK")
    rejected_emp.append(name)


try:
    exp>age
except:ValueError
print("Invalid Input!! please verify ")
demo=selected_emp.pop()


print("SELECTED EMPLOYEES LIST :",selected_emp)

print("REJECTED EMPLOYEE LIST :",rejected_emp)



print("THANK YOU!! For Joining")


