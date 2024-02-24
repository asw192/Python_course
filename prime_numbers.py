final_number = int(input("Input the number to which prime numbers need calculated"))

start_number=2

print("Prime numbers between", start_number, "and", final_number, "are:")

for num in range(start_number,final_number+1):
    for i in range(2,num):
        if(num%i) == 0:
            break
    else:
        print(num)
    
