def greatest_common_divisor(x,y):
    print "For", x, "and", y,","  
    remainder = x % y
    while remainder > 0:
        remainder = x % y
        if remainder == 0: 
            print "The Greatest Common Divisor: ", y,"."
        else:
            temp = y
            x = temp
            y = remainder

greatest_common_divisor(11, 99)
