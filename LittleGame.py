import random as rd
def menu():
    while True:
        print("功能選項")
        print("(1)猜數字遊戲")
        print("(2)幾A幾B遊戲")
        print("(3)井字遊戲(雙人遊戲)")
        print("(4)井字遊戲(單人遊戲)")
        print("(5)離開程式Exit")
        n = eval(input("請輸入數字選擇遊戲:"))
        if n == 1:
            print("進入(1)猜數字遊戲(1~99)")
            guestnumber()
        elif n == 2:
            print("進入(2)幾A幾B遊戲(第一位數可為0,位置及數字對為A,位置錯數字對為B)")
            nAnB()
        elif n == 3:
            print("進入(3)井字遊戲(o為先手,x為後手)")
            ooxx1()
        elif n == 4:
            print("進入(4)井字遊戲(單人遊戲,玩家為先手)")
            ooxx2()
        elif n == 5:
            print("即將離開程式")
            break
        else:
            #若輸入1~5以外的數字，則重複進入功能選項
            print("輸入錯誤")
            print("重新進入功能選項")
            continue

def guestnumber():
    guestnumber=rd.randint(1,99)
    correct=0
    comparenumber=[0,100]
    while correct!=1:
        n=eval(input("輸入一個0~99的數字:"))
        #判斷是否輸入區間內的數字
        if n<1 or n>99:
            print("輸入錯誤")
        elif n==guestnumber:
            print("恭喜猜對數字")
            print("回到功能選項")
            correct=1
        else:
            if n not in comparenumber:
                comparenumber.append(n)
                comparenumber.sort()
                for i in range(len(comparenumber)):
                    if comparenumber[i]>guestnumber:
                        print("{},{}之間猜一個數:".format(comparenumber[i-1],comparenumber[i]))
                        break
            else:
                print("以輸入過此數字")
            
def nAnB():
    #產出四個不重複亂數，並以一維串列儲存
    guestnumber=[]
    count=0
    count1=0
    A=0
    B=0
    while count<4:
        randomnum=rd.randint(0,9)
        if randomnum not in guestnumber:
            guestnumber.append(randomnum)
            count+=1
    #當未猜出數字時讓使用者重複輸入及判斷
    while A!=4:
        #判斷使用者輸入數字是否有重複
        while count1!=4:
            comparenumber=[]
            n=eval(input("輸入一個四位數字,且不重複:"))
            #千位數
            comparenumber.append(n//1000)
            count1+=1
            #百位數
            if (n%1000//100) not in comparenumber:
                comparenumber.append((n%1000//100))
                count1+=1
            #十位數
            if (n%100//10) not in comparenumber:
                comparenumber.append((n%100//10))
                count1+=1
            #個位數
            if (n%10) not in comparenumber:
                comparenumber.append((n%10))
                count1+=1
            if len(comparenumber)!=4:
                print("輸入錯誤")
                count1=0
        A=0
        B=0
        #判斷位置及數字正確的數量(A的數量)
        for i in range(4):
            if guestnumber[i]==comparenumber[i]:
                A+=1
        #判斷位置錯誤,數字正確的數量(B的數量)
        for i in range(4):
            for j in range(4):    
                if i!=j and guestnumber[i]==comparenumber[j]:
                    B+=1
        print("{}A{}B".format(A,B))
        if A!=4:
            count1=0
        elif A==4:
            print("恭喜猜對數字")
            print("回到功能選項")

def ooxx1():
    #畫出井字畫面
    number=[]
    for i in range(9):
        number.append(i)
        if (i+1)%3!=0:
            print("{}|".format(number[i]),end="")
        else:
            print("{}\n".format(number[i]),end="")
            if i<6:
                print("一一一",end="\n")
    v=0
    count=0       
    playernumber=[]*9
    while v!=1:
        player1=eval(input("請玩家一輸入想選擇的位置:"))
        while player1 in playernumber:
            player1=eval(input("此位置已被選過,請重新輸入:"))
        if player1 not in playernumber:
            playernumber.append(player1)
            count+=1
            number[player1]="O"
            for i in range(9):
                if (i+1)%3!=0:
                    print("{}|".format(number[i]),end="")
                else:
                    print("{}\n".format(number[i]),end="")
                    if i<6:
                        print("一一一",end="\n")
            #判斷輸贏
            for i in range(0,7,3):
                #判斷橫排
                if number[i]==number[i+1]==number[i+2]:
                    print("玩家一獲勝")
                    print("回到功能選項")
                    v=1
                    break
            for i in range(0,3):
                #判斷直排
                if number[i]==number[i+3]==number[i+6]:
                    print("玩家一獲勝")
                    print("回到功能選項")
                    v=1
                    break
            #判斷對角線
            if number[0]==number[4]==number[8]:
                    print("玩家一獲勝")
                    print("回到功能選項")
                    v=1
                    break
            if number[2]==number[4]==number[6]:
                print("玩家一獲勝")
                print("回到功能選項")
                v=1
                break
            if count==9:
                print("平手")
                print("回到功能選項")
                break
        player2=eval(input("請玩家二輸入想選擇的位置:"))
        while player2 in playernumber:
            player2=eval(input("此位置已被選過,請重新輸入:"))
        if player2 not in playernumber:
            playernumber.append(player2)
            count+=1
            number[player2]="X"
            for i in range(9):
                if (i+1)%3!=0:
                    print("{}|".format(number[i]),end="")
                else:
                    print("{}\n".format(number[i]),end="")
                    if i<6:
                        print("一一一",end="\n")
            #判斷輸贏
            for i in range(0,7,3):
                #判斷橫排
                if number[i]==number[i+1]==number[i+2]:
                    print("玩家二獲勝")
                    print("回到功能選項")
                    v=1
                    break
            for i in range(0,3):
                #判斷直排
                if number[i]==number[i+3]==number[i+6]:
                    print("玩家二獲勝")
                    print("回到功能選項")
                    v=1
                    break
            #判斷對角線
            if number[0]==number[4]==number[8]:
                    print("玩家二獲勝")
                    print("回到功能選項")
                    v=1
                    break
            if number[2]==number[4]==number[6]:
                    print("玩家二獲勝")
                    print("回到功能選項")
                    v=1
                    break
             
def ooxx2():
     #畫出井字畫面
    number=[]
    for i in range(9):
        number.append(i)
        if (i+1)%3!=0:
            print("{}|".format(number[i]),end="")
        else:
            print("{}\n".format(number[i]),end="")
            if i<6:
                print("一一一",end="\n")
    v=0 
    count=0       
    playernumber=[]*9
    while v!=1:
        player1=eval(input("請玩家輸入想選擇的位置:"))
        while player1 in playernumber:
            player1=eval(input("此位置已被選過,請重新輸入:"))
        if player1 not in playernumber:
            playernumber.append(player1)
            count+=1
            number[player1]="O"
            for i in range(9):
                if (i+1)%3!=0:
                    print("{}|".format(number[i]),end="")
                else:
                    print("{}\n".format(number[i]),end="")
                    if i<6:
                        print("一一一",end="\n")
            #判斷輸贏
            for i in range(0,7,3):
                #判斷橫排
                if number[i]==number[i+1]==number[i+2]=="O":
                    print("玩家獲勝")
                    print("回到功能選項")
                    v=1
                    break
            for i in range(0,3):
                #判斷直排
                if number[i]==number[i+3]==number[i+6]:
                    print("玩家獲勝")
                    print("回到功能選項")
                    v=1
                    break
            #判斷對角線
            if number[0]==number[4]==number[8]:
                    print("玩家獲勝")
                    print("回到功能選項")
                    v=1
                    break
            elif number[2]==number[4]==number[6]:
                    print("玩家獲勝")
                    print("回到功能選項")
                    v=1
                    break
            elif count==9:
                print("平手")
                print("回到功能選項")
                break
        computer=rd.randint(0,8)       
        while computer in playernumber:
            computer=rd.randint(0,8)  
        if computer not in playernumber:
            print("電腦選擇{}的位置:".format(computer))
            playernumber.append(computer)
            count+=1
            number[computer]="X"
            for i in range(9):
                if (i+1)%3!=0:
                    print("{}|".format(number[i]),end="")
                else:
                    print("{}\n".format(number[i]),end="")
                    if i<6:
                        print("一一一",end="\n")
            #判斷輸贏
            for i in range(0,7,3):
                #判斷橫排
                if number[i]==number[i+1]==number[i+2]:
                    print("電腦獲勝")
                    print("回到功能選項")
                    v=1
            for i in range(0,3):
                #判斷直排
                if number[i]==number[i+3]==number[i+6]:
                    print("電腦獲勝")
                    print("回到功能選項")
                    v=1
                    break
            #判斷對角線
            if number[0]==number[4]==number[8]:
                print("電腦獲勝")
                print("回到功能選項")
                v=1
                break
            elif number[2]==number[4]==number[6]:
                print("電腦獲勝")
                print("回到功能選項")
                v=1
                break   
                        
menu()