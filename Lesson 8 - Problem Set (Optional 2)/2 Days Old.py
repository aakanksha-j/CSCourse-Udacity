# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days.
# Account for leap days.
#
# Assume that the birthday and current date are correct dates (and no
# time travel).
#

def daysBetweenDates(year1, month1, day1, year2, month2, day2):

    def inBetweenMonths(month):
        i=month
        if i==1:
            month_days=31
        if i==2:
            month_days=28
        if i==3:
            month_days=31
        if i==4:
            month_days=30
        if i==5:
            month_days=31
        if i==6:
            month_days=30
        if i==7:
            month_days=31
        if i==8:
            month_days=31
        if i==9:
            month_days=30
        if i==10:
            month_days=31
        if i==11:
            month_days=30
        if i==12:
            month_days=31
        return month_days

    def dateDays(year1, month1, day1, year2, month2, day2):
        z=0
        if month1==month2 and year1==year2:
            z=day2-day1
        else:
            z1=inBetweenMonths(month1)-day1
            z=z1+day2

        #print z
        return z

    def monthDays(year1, month1, year2, month2):
        y=0
        if year1==year2:
            i=month1+1
            while i<month2:
                y=inBetweenMonths(i)
                i=i+1

        else:
            i,j,y1,y2=month1+1, month2-1, 0, 0
            while i<=12:
                y1=y1+inBetweenMonths(i)
                #print 'y1 inside loop:',y1
                i=i+1
            #print 'y1 outside loop:',y1
            while j>0:
                y2=y2+inBetweenMonths(j)
                #print 'y2 inside loop:',y2
                j=j-1
            #print 'y2 outside loop:',y2
            y=y1+y2

        #print y
        return y

    def yearDays(year1, year2):
        x=0
        if year2-year1>1:
             x=(year2-year1-1)*365

        #print x
        return x

    def leapYear(year):
        if (year%400==0) or (year%100!=0 and year%4==0):
            return True
        else:
            return False

    def leapDays(year1, month1, day1, year2, month2, day2):
        u=0

        u3=0
        if year1==year2:
            if leapYear(year1) and month1!=month2 and month1<=2 and month2>2:
                u3=1
        else:
            u1,u2=0,0
            if leapYear(year1) and month1<=2:
                u1=1
            if leapYear(year2) and ((month2==2 and day2>28) or (month2>2 and day2>=1)):
                u2=1
            u3=u1+u2

        u4=0
        i=year1+1
        while i<year2:
            if leapYear(i):
                u4=u4+1
            i=i+1

        u=u3+u4
        #print u
        return u

    noOfDays=dateDays(year1, month1, day1, year2, month2, day2)+monthDays(year1, month1, year2, month2)+yearDays(year1, year2)+leapDays(year1, month1, day1, year2, month2, day2)
    print 'No of days between dates:',noOfDays
    return noOfDays

# Test routine

def test():
    test_cases = [((1963,10,4,1965,7,27), 662),
                  ((1963,10,4,1992,2,24), 10370),
                  ((1963,10,4,2003,10,14), 14620),
                  ((1965,7,27,1992,2,24), 9708),
                  ((1965,7,27,2003,10,14), 13958),
                  ((1987,12,1,1992,2,24), 1546),
                  ((1987,12,1,2003,10,14), 5796),
                  ((1992,2,24,2003,10,14), 4250),]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            #print "Test case passed!"
            print "Test with data:", args, "passed"

test()
