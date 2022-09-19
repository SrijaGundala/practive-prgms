def sumDigitSquare( n):
    sq = 0;
    while (n!=0):
        digit = n % 10
        sq += digit * digit
        n = n // 10
         
    return sq;

def isHappy(n):
    
    s=set()
    s.add(n)
    while (True):
 
        
        if (n == 1):
            return True;

        n = sumDigitSquare(n)
 
        
        if n in s:
            return False
 
        # Mark n as visited
        s.add(n)
 
    return false;
