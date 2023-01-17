
def addition(a:int,b:int)->int:
    """The addition function should take in two integers a and b and add them together and returns its sum as integer.
    The addition function will return -1 if either parameter are not integers, or if their sum is above 1000 or below 0
    
    Args:
        a (int): parameter 1
        b (int): parameter 2

    Returns:
        int: result of a + b. Returns -1 if a+b > 1000 or a+b < 0
    """
    #here is an implementation in if, elif, and else assuming that a and b are integers.
    
    if isinstance(a,int) == isinstance(b,int) == True:
        sum = a+b
        if 0 <=sum<= 1000:
            return sum
        else:
            return -1
    else:
        return -1    
    
        
    
    
    
    
    # Now, do not assume that the parameters are integers.
    # use try, except, finally for the following code implementation
    
    return -1 # delete this when you finish your code



if __name__ == "__main__":
    while(True):
        userInput1 = input("Please input the first number: ")
        userInput2 = input("Please input the second number: ")
        
        rst = addition(userInput1,userInput2)
        print("result:", rst)
    
