def main():
    
    nterms = int(input("how many terms?"))

    def recurs(n):
        if n==1:
            return 0
        elif n==2:
            return 1
        else:
            return recurs(n-1)+recurs(n-2)

    for i in range(1,nterms):
        print(recurs(i))
main()