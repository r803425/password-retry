password = 'a123456'
pwd = input('請輸入密碼: ')
count = 3
out_of_limit = False

while True:
    count = count - 1
    if pwd == password:
        print('登入成功')
        break
    elif count == 0:
        print('你沒機會了，傻B')
        break
    elif pwd != password and not out_of_limit:
        print('密碼錯誤!還有', count, '次機會')
        pwd = input('請輸入密碼: ')