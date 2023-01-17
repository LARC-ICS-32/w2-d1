


def foo():
    """
    Complete the foo function so that every error is catched properly without triggering excess exceptions
    After completing an error problem, comment out the line that causes the error so and proceed next.
    
    Please do not use a single except to catch everything, that defeats the purpose of this practice.
    It is also a good practice to write the error that which the line causes in the comment.
    


    """
    print("\033[96mStart of foo()","\033[0m")
    try:
        
        # ERROR 1
        a = 0
        b = 1
        c = a/b # c=?
        d = b/a # d=?, what error will this cause? 
        
        
        # ERROR 2
        a = [1,2,3,4]
        b = [5,6,7,8]
        c = a+b # c=?
        d = a-b # d=?, what error will this cause? 
        
        
        # ERROR 3
        a = "Hello "
        b = "World"
        c = a+b # c=?
        d = int(a) + int(b) # d=?, what error will this cause?

        
        # ERROR 4
        a = [1,2,3,4]
        print(a[5]) # what error will this cause?

        
        # ERROR 5
        class o:
            def __init__(self):
                self.a = 1
                self.b = 2
                
        a = o()
        c = a.a+a.b
        print(a.c) # what error will this cause? 
        
        
        # ERROR 6
        # make your custom exceptions class here and raise it along with a message saying "yourError is raised but not catched properly"
        # make sure to catch it in the exceptions!
        
        
        
        
        
        
    finally:
        print("\033[96mEnd of foo()","\033[0m")
    

if __name__ == "__main__":
    try:
        print()
        foo()
        print("\033[92mYou have successfully handled all exceptions in your code","\033[0m")
    except Exception as ex:
        print("\033[93myou did not handle all of the exceptions, you missed this:\033[91m",ex,"\033[0m")
    
    
        
    

