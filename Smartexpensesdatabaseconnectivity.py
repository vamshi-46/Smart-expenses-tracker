import mysql.connector as mq
con=mq.connect(host='localhost',password='manager',user='root')

if con.is_connected():
    print("Connected successfully")

cur=con.cursor()
cur.execute("use emp")


while True:
    print('1...... Expendure ')
    print('2...... Show Savings')
    print('3...... Monthly expenditure')
    print('4...... Heads')
    print('5...... Show Trips')
    print('6...... Max and Min expenditure of year')
    print('7...... Exit')
    choice=int(input('Enter Choice ....'))
    if choice==1:
        month=input('enter month name ')
        basic=int(input('enter basic sal for month'))
        exp=[]
        head=[]
        while True:
            hd=input('enter head')
            head.append(hd)
            ex=int(input('enter expendure'))
            exp.append(ex)
            try:
                cur.execute('Insert into heads(Month,Head,Exp) values(%s,%s,%s)',(month,hd,ex))
            except mysql.connecter.Error as err:
                con.close()
            ch=input('any more :- y/n')
            if ch=='n' or ch=='N':
                break
        sum=0
        for i in exp:
            sum=sum+i
        bal=basic-sum
        cur.execute('Insert into empexp(Basicsal,Month,Totexp,Monthbal) values(%s,%s,%s,%s)',(basic,month,sum,bal))
        con.commit()
    elif choice==2:
        print("1-monthexp,bal;  2-Total savings")
        ch=int(input("1/2"))
        if ch==1:
            cur.execute("use emp")
            month=input('enter month name ')
            my=(month,)
            q='select Totexp,Monthbal from empexp where Month=%s'
            cur.execute(q,my)
            for i in cur:
                print(i)
        else:
            s="select sum(Monthbal) from empexp"
            cur.execute(s)
            for i in cur:
                print(i)
    elif choice==3:
        cur.execute("use emp")
        q='select Month,Basicsal,Totexp from empexp'
        cur.execute(q)
        print("Month Basicsal Totexp")
        for i in cur:
            print(i)
    elif choice==4:
        q='select Head,sum(Exp) from heads group by Head'
        cur.execute(q)
        for i in cur:
            print(i)
    elif choice==5:
        q1='select sum(Monthbal) from empexp'
        cur.execute(q1)
        for i in cur:
            i1=int("".join(map(str,i)))
            if i1>50000:
                print('Trip To abrad',i1)
            elif i1>25000:
                print('Trip within country',i1)
            elif i1>10000:
                print('Week end Trip',i1)
            else:
                print('No savings',i1)
    elif choice==6:
        #q2='select Month,min(Totexp),max(Totexp) from empexp group by Month'
        #q1='select Month from empexp group by Month having max(Totexp) =(select max(Totexp) from empexp)'
        q1='select Month,Totexp from empexp where Totexp =(select max(Totexp) from empexp)'
        cur.execute(q1)
        for i in cur:
            print(i)
        q2='select Month from empexp group by Month having min(Totexp) =(select min(Totexp) from empexp)'
        cur.execute(q2)
        for i in cur:
            print(i)
    elif choice==7:
        break
'''cur.execute("use emp")
s="select * from empexp"
cur.execute(s)
for i in cur:
    print(i)
con.commit()'''
    
    
            
