aa = 3
ans = 'a123456'
while True:
    psw = input('請輸入密碼:')
    aa = aa - 1
    if psw == ans:
        print('登入成功!')
        break
    elif psw != ans:
        print('密碼輸入錯誤,還有',aa,'次')
        if aa == 0:
            print('以輸入3次錯誤,系統將封鎖!')
            break
