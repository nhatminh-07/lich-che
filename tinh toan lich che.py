import time
class yeartypes:
    def __init__(self, sy, leap):
        self.sy = sy
        self.leap = leap

class dateyears:
    def __init__(self, date, month, year):
        self.date = date
        self.month = month
        self.year = year

    def __str__(self):
        dmn = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        return f"{self.date} {dmn[self.month-1]}, {self.year}"
    
tt = [0, 80, 168, 248, 336, 416, 504, 584, 664, 752, 832, 920, 1000]
tlep = [0, 21, 38, 59, 78, 99, 118, 139, 160, 179, 200, 219, 240]

def returnmonth(Y): 
    for i in range(1, 13):
        if tt[i]>=Y: return i

def dmy(d, m):
    res = 0
    if (m==1): res = d
    elif (m==2): res = d+31
    elif (m==3): res = d+59
    elif (m==4): res = d+90
    elif (m==5): res = d+120
    elif (m==6): res = d+151
    elif (m==7): res = d+181
    elif (m==8): res = d+212
    elif (m==9): res = d+243
    elif (m==10): res = d+273
    elif (m==11): res = d+304
    elif (m==12): res = d+334
    return res

def calnhuan(Y, leap):
    res = 0
    if leap and Y>=168: res +=1
    cmn = returnmonth(Y)
    a = Y-tt[cmn-1]
    if (cmn in [1, 3, 5, 7, 8, 10, 12]): res = tlep[cmn-1] + a//4 + a//79
    elif cmn==2: res = tlep[cmn-1] + a//5
    else: res = tlep[cmn-1] + a//5 + a//84 + a//88
    return res

def cntleapyear(y):
    if y==0: return 0
    x = startingwith(str((y-1)//1000))
    lcount = x.leap
    return 240*((y-1)//1000) + cntleapyear((y-1)//1000) + calnhuan((y-1)%1000+1, lcount)

def cntdays():
    d = int(input("Select days: "))
    m = int(input("Select month: "))
    y = int(input("Select years: "))
    x = startingwith(str(y))
    c = 0
    if m<=2 and x.leap: c -= 1
    c += (365*(y-1))+dmy(d, m)+cntleapyear(y)
    print(c)

def printso(n):
    if n<=0: print("  ", end=" ")
    elif n<10: print(" "+str(n), end=" ")
    else: print(n, end=" ")

def printth(length, rem):
    print("T2 T3 T4 T5 T6 T7 CN")
    for i in range((length-rem+13)//7): #so dong can in
        for j in range(7):
            ann = i*7+j+1+rem-7
            if ann<=length: printso(ann)
        print()

def printyr(days, rem):
    ptlist = [7, 4, 4, 1, 6, 3, 1, 5, 2, 7, 4, 2] #if rem=7 with days=365
    length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    length[1] += (days-365)
    for i in range(2, 12):
        ptlist[i] = (ptlist[i]+(372-days)-1)%7+1

    for i in range(12):
        print(f"Tháng {i+1}")
        #print((ptlist[i]+rem-1)%7+1)
        printth(length[i], (ptlist[i]+rem-1)%7+1)

def callist(Y, leap):
    res = 0
    if leap and Y>=168: res +=1
    cmn = returnmonth(Y)
    a = Y-tt[cmn-1]
    if (cmn in [1, 3, 5, 7, 8, 10, 12]): res = Y + tlep[cmn-1] + a//4 + a//79
    elif cmn==2: res = Y + tlep[cmn-1] + a//5
    else: res = Y + tlep[cmn-1] + a//5 + a//84 + a//88
    return (7-res%7)%7+1

def isleap(Y, leap):
    cmn = returnmonth(Y)
    if leap and Y==168: return True
    a = Y-tt[cmn-1]
    if (cmn in [1, 3, 5, 7, 8, 10, 12]): return (a%4==0 or a==79)
    elif cmn==2: return (a%5==0)
    else: return (a%5==0 or a==84 or a==88)

def startingwith(n):
    if (len(n)%3==1): n = "00"+n
    elif (len(n)%3==2): n = "0"+n

    #print(n)

    arr=[]
    for i in range(0, len(n), 3):
        arr.append(int(n[i:i+3]))
    

    if arr[-1]==0: arr[-1]=1000

    for i in range(len(arr)-2, -1, -1):
        if arr[i]== 0 and arr[i+1]==1000: arr[i]=1000
        elif arr[i+1]!=1000: arr[i]+=1
    
    arr = [1]+arr
    #print(*arr)

    x = 0
    leap = False
    for i in range(len(arr)):
        x += callist(arr[i], leap)
        leap = isleap(arr[i], leap)
    
    return yeartypes(x, leap)

def lichnam():
    n = input("Select years: ")

    yr = startingwith(n)
    x = yr.sy
    leap = yr.leap

    printyr(365 + leap, (x-1+leap)%7+1)

def tinhthu(d, m, n):
    yr = startingwith(n)
    x = yr.sy
    leap = yr.leap

    kq = dmy(d, m)
    #print(kq)
    if leap and m>=3: kq += 1

    thu = (kq - x + 7)%7
    if (thu==1): print("Monday,", dateyears(d, m, n))
    elif (thu==2): print("Tuesday,", dateyears(d, m, n))
    elif (thu==3): print("Wednesday,", dateyears(d, m, n))
    elif (thu==4): print("Thursday,", dateyears(d, m, n))
    elif (thu==5): print("Friday,", dateyears(d, m, n))
    elif (thu==6): print("Saturday,", dateyears(d, m, n))
    elif (thu==0): print("Sunday,", dateyears(d, m, n))

def nextdays(d, m, n, nd):
    for _ in range(nd):
        isleap = startingwith(n).leap
        length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (isleap): length[1]=29
        if (d==length[m-1]):
            if m==12: 
                m= 1
                n = str(int(n)+1)
            else: m += 1
            d = 1
        else: d += 1
        tinhthu(d, m, n)
        #time.sleep(0.25)

def main():
    print("List functions:")
    print("1. Write the year calendar")
    print("2. Check the days of the week")
    print("3. Count the number of days since the start")
    print("4. Count tomorrow and other days")
    options = int(input("Choose functions: 1 / 2 / 3 / 4: "))
    if (options==1): lichnam()
    elif (options==2): 
        d = int(input("Select days: "))
        m = int(input("Select month: "))
        n = input("Select years: ")
        tinhthu(d, m, n)
    elif (options==3): cntdays()
    else: 
        d = int(input("Select days: "))
        m = int(input("Select month: "))
        n = input("Select years: ")
        nd = int(input("Number of days: "))
        nextdays(d, m, n, nd)

if __name__=="__main__":
    main()
