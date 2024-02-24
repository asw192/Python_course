nfactorial = int(input("Input the number of which factorial needs calculated"))

factorial=1

if nfactorial<0:
    print("Negative number doesnt have factorial")
elif nfactorial==0:
    print("Factorial of zero is 1")
else:
    for i in range(1,nfactorial+1):
        factorial=factorial*i
    print("The factorial of",nfactorial,"is",factorial)
