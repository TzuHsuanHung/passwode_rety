password = 'a123456' 
n = 3 #剩餘機會

while True:
	answer = input('請輸入密碼：')
	if password == answer:
		print('登入成功!')
		break #逃出迴圈
	else:
		n = n - 1
		print('密碼錯誤！還有', n , '次機會')
		if n == 0:
			break
