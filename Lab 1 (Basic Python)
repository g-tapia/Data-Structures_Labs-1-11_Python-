def is_perfect(n):
    sum = 0
    for x in range(1,n):
        if(n % x == 0):
            sum = sum + x
    if sum == n:
        return True
    else:
        return False
    pass


def multiples_of_3_and_5(n):
    sum = 0
    for x in range(1,n):
        if x%3 == 0 or x%5==0:
            sum+=x
    return(sum)
    pass
    
    
def integer_right_triangles(p):
    counter=0
    for x in range(1,p//2):
        for z in range(x+1,p//2):
            y=p-(x+z)
            if x+z > y and z+y > x and x+y > z:
                if x*x + z*z==y*y:
                    counter=counter+1
    return counter
   
   
def gen_pattern(chars):
    m=len(chars)
    for y in range(1,2*m):
        z = -y
        if(y>m):
            z=y%m
        string1 = chars[z:]
        string2 = string1[1:]
        
        string2 = string2[::-1]
        
        s = '.'.join(string2+string1)
        
        print(s.center(4*m - 3, '.'))
