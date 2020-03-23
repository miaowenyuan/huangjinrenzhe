"""Pam_Case_Profile = {'Affluent':
                    {'description': "Job = Locate Mr.Muggles, the client's cat. Client=I.m.Affluent.",
                    'tags': 'rich client,spoiled cat, consider butler',
                    'ID':'000001',
                    'date':'2020.01.01'},
                   'Miaowenyuan':
                    {'description': "Job = Locate Ms.Wangruoyue, the client's friend. Client=Miaowenyuan.",
                    'tags': 'poor client,missed friend, consider LA',
                    'ID':'000002',
                    'date':'2020.02.01'}}

"""

fr = open("registry.txt",'r+')
dic = eval(fr.read()) #读取的str转换为字典
print(dic)
fr.close()


Pam_Case_Profile=dic
print('|-----welcome to case registry-----|')
print('|------- 1:Show all cases -------|')
print('|------- 2:Search all cases -----|')
print('|------- 3:Add a new case -------|')
print('|------- 4:Modify an case -------|')
print('|------- 5:Quit -------|')
print('\n')
while 1:
    temp = input('please input command：')
    guess = int(temp)
    if guess == 1:
        print('All cases are listed below:')
        for key in Pam_Case_Profile.keys():
            print(key,':',Pam_Case_Profile[key])
            print('\n')


    if guess == 2:
        search= input('please input the keywods：')
        for name in Pam_Case_Profile.keys():
            if search in Pam_Case_Profile[name]['tags']:						
                print(name,':',Pam_Case_Profile.get(name))
                print('\n')
            elif search in Pam_Case_Profile[name]['description']:
                print(name,':',Pam_Case_Profile.get(name))
                print('\n')
            else:
                print('sorry，this client dose not exist，please input again!')
                print('\n')
            

    if guess == 3:
        Add = input('please input new client name：')
        b = {Add : {'description':'','tags':'','ID':'','date':''}}	
        Pam_Case_Profile.update(b)
        
        description_val = input('please input description：')
        c = {'description' : description_val}	
        Pam_Case_Profile[Add].update(c)
        
        tags_val = input('please input tags：')
        d = {'tags' : tags_val}	
        Pam_Case_Profile[Add].update(d)
        
        ID_val = input('please input ID：')
        e = {'ID' : ID_val}	
        Pam_Case_Profile[Add].update(e)
        
        date_val = input('please input date：')
        f = {'date' : date_val}	
        Pam_Case_Profile[Add].update(f)
        print('\n')

        fw = open("registry.txt",'w+')
        fw.write(str(Pam_Case_Profile)) #把字典转化为str
        fw.close()    
            
    if guess == 4:
        Modify=input('please input the client you want to modify:')
        if Modify in Pam_Case_Profile.keys():
            print('the name you input exist in Database--->',end= ' ')
            print(Modify,':',Pam_Case_Profile[Modify])
            confirm = input('do you want to modify the profile（yes/no）：')
            if confirm == 'yes':
                description_val1 = input('please input new description：')
                h = {'description' : description_val1}	
                Pam_Case_Profile[Modify].update(h)
                print('\n')
                
                tags_val1 = input('please input new tags：')
                i = {'tags' : tags_val1}	
                Pam_Case_Profile[Modify].update(i)
                print('\n')
                
                ID_val1 = input('please input new ID：')
                j = {'ID' : ID_val1}	
                Pam_Case_Profile[Modify].update(j)
                print('\n')
                
                date_val1 = input('please input new date：')
                k = {'date' : date_val1}	
                Pam_Case_Profile[Modify].update(k)
                print('\n')

                fw = open("registry.txt",'w+')
                fw.write(str(Pam_Case_Profile)) #把字典转化为str
                fw.close()
            else:
                print('\n')
                break
        else:
            print('the name you input does not exist --->',end= ' ')
            break
            
    if guess == 5:
        print('|-----Thanks for using registry-----|')
        print('\n')
        break
    print('|-----welcome to case registry-----|')
    print('|------- 1:Show all cases -------|')
    print('|------- 2:Search all cases -----|')
    print('|------- 3:Add a new case -------|')
    print('|------- 4:Modify an case -------|')
    print('|------- 5:Quit -------|')
    print('\n')
