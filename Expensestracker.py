list=[]
heads=dict()
class Heads:
    def __init__(self,hname):
        self.hname=hname
while True:
    print('1...... Create ')
    print('2...... Show Savings')
    print('3...... Monthly expenditure')
    print('4...... Heads')
    print('5...... Show Trips')
    print('6...... Max and Min expenditure of year')
    print('7...... Exit')
    choice=int(input('Enter Choice ....'))
    class project:
        def __init__(self,name,month,salary,heads):
            self.heads=heads
            self.sal=salary
            self.name=name
            self.month=month
            self.salary=salary
            self.exp=0
        def expendure(self,head,amt):
            self.head=head
            self.amt=amt
            self.heads[self.head]=self.amt
            self.exp=self.exp+self.amt
            self.salary=self.salary-self.amt
        def display(self):
            print('Emp Name           .....  ',self.name)
            print('Emp Month          .....  ',self.month)
            print('Emp Expendure      .....  ',self.exp)
            print('Emp Balance Sal    .....  ',self.salary)
            print()

    if choice==1:
        na=input('enter emp name  ')
        mon=input('enter month name ')
        sal=int(input('enter salary '))
        heads=dict()
        e=project(na,mon,sal,heads)
        
        flag=True
        while flag:
            ht=int(input('enter head 1-rent 2-elecbill 3-grossary 4-chilfee'))
            at=int(input('enter expenditure '))
            if ht==1:
                hd='rent'
            elif ht==2:
                hd='elecbill'
            elif ht==3:
                hd='grossary'
            elif ht==4:
                hd='chilfee'
            e.expendure(hd,at)
            ch=input('any more to enter y/n..')
            if ch=='n' or ch=='N':
                flag=False
        list.append(e)
        #print(heads)
            
    elif choice==2:
        for i in list:
            i.display()

            i=0
        tb=0
        while i<len(list):
            tb=tb+list[i].salary
            i+=1
        print('\n Total savings',tb)
    elif choice==3:
        i=0
        while i<len(list):
            print('Month :- ',list[i].month,'Income :- ',list[i].sal,'Expendure :- ',list[i].exp)
            i+=1
    elif choice==4:
        tr=0
        te=0
        tg=0
        tc=0
        for i in list:
            e=0
            for j in i.heads.items():
                if j[e]=='rent':
                    tr=tr+i.heads.get('rent')
                elif j[e]=='elecbill':
                    te=te+i.heads.get('elecbill')
                elif j[e]=='grossary':
                    tg=tg+i.heads.get('grossary')
                else:
                    tc=tc+i.heads.get('chilfee')
        hexp=tr
        pos=1
        if te>hexp:
            hexp=te
            pos=2
        elif tg>hexp:
            hexp=tg
            pos=3
        elif tc>hexp:
            hexp=tc
            pos=4

        if pos==1:
            print('Hexp is Rent :- ',tr)
        elif pos==2:
            print('Hexp is Elec Bill :- ',te)
        elif pos==3:
            print('Hexp is Grossary  :- ',tg)
        else:
            print('Hexp is Children Fee :- ',tc)
                    
    elif choice==5:
        i=0
        tb=0
        while i<len(list):
            tb=tb+list[i].salary
            i+=1
        if tb>50000:
            print('Trip To abrad',tb)
        elif tb>25000:
            print('Trip within country',tb)
        elif tb>10000:
            print('Week end Trip',tb)
        else:
            print('No savings',tb)
    elif choice==6:
        te=[]
        tg=[]
        tc=[]
        for i in list:
            e=0
            for j in i.heads.items():
                if j[e]=='elecbill':
                    te.append(i.heads.get('elecbill'))
                elif j[e]=='grossary':
                    tg.append(i.heads.get('grossary'))
                else:
                    tc.append(i.heads.get('chilfee'))
        while True:
            print('\n1-elecbill  2-grossary  3-chilfee  4-exit')
            c=int(input('Enter choice 1/2/3 to check max and min head in year'))
            if c==1:
                print('Max elecbill - ',max(te),'Min elecbill - ',min(te))
            elif c==2:
                print('Max grossary - ',max(tg),'Min grossary - ',min(tg))
            elif c==3:
                print('Max chilfee - ',max(tc),'Min chilfee - ',min(tc))
            else:
                break
    else:
        break
            







    
    
    
    
