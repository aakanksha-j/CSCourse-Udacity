# Define a procedure, stamps, which takes as its input a positive integer in
# pence and returns the number of 5p, 2p and 1p stamps (p is pence) required 
# to make up that value. The return value should be a tuple of three numbers 
# (that is, your return statement should be followed by the number of 5p,
# the number of 2p, and the nuber of 1p stamps).
#
# Your answer should use as few total stamps as possible by first using as 
# many 5p stamps as possible, then 2 pence stamps and finally 1p stamps as 
# needed to make up the total.
#
# (No fair for USians to just say use a "Forever" stamp and be done with it!)
#

def stamps(n):
    p5,p2,p1=0,0,0
    if n%5.0>=0:
       p5=n/5
       mod5=n%5
       if mod5>0:
           p2=mod5/2
           mod2=mod5%2
           if mod2>0:
               p1=1
    else:
        if n%2.0>=0:
            p2=n/2
            mod2=n%2
            if mod2>0:
                p1=1
        else:
            if n==1:
                p1=1
                
            
    return p5, p2, p1