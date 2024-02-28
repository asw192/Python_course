def main():  

  

    ls = [12, 70, -4, 16, 22]  

    ## Type your code blow:  
    def calc_average(my_list):
        mul_out = 1
        import math
        summer = sum(my_list)
        mul_out = summer/len(ls)
        
        return mul_out  


    result = calc_average(ls)  
 

    print(result)  

    return result 


main() 