def main():

    nfactorial = int(input("Input the number of which factorial needs calculated"))

    def funcfactorial(number):

        if (number==0 or number==1):
            return number
        else:
            return (number*funcfactorial(number-1))

           
    print(funcfactorial(nfactorial))
main()
