password = 'a123456'
count = 3 #剩餘機會
out_of_limit = False

while count > 0: #要重複做，所以使用while loop
    count = count - 1
    pwd = input('請輸入密碼: ') #要寫在這裡，重複要做的事情
    if pwd == password:
        print('登入成功')
        break #登入成功，馬上逃出迴圈
    else: # pwd != password and not out_of_limit:
        print('密碼錯誤!')
        if count > 0:
            print('還有', count, '次機會')
        else:
            print('你沒機會了，傻B')
            #break #沒機會了，馬上逃出迴圈