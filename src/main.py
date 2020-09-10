def greatest_common_divisor(x,y):
    print "For", x, "and", y,","  
    r=x%y
    while r>0:
        r=x%y
        if r ==0: 
            print "the Greatest Common Divisor: ", y,"."
        else:
            z=y
            x=z
            y=r

greatest_common_divisor(11, 99)
