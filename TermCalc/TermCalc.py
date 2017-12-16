print ('Hi, Welcome to TermCalc.')
num1=int(input("Enter Your First Number: "))
print ('P.S. + = Addition, - = Subtraction, x = Multiplcation, and / = Division')
func=input("function +, -, x, / :")
num2=int(input("Enter Your Second Number: "))

if func=="+":
    ans=num1+num2
    print(ans)
else:
    pass

if func=="-":
    ans=num1-num2
    print(ans)
else:
    pass

if func=="x":
    ans=num1*num2
    print(ans)
else:
    pass

if func=="/":
    ans=num1/num2
    print(ans)
else:
    pass
