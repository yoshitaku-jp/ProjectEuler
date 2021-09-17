# num1,num2を足して行って、偶数ならsumに足す。
num1 = 1
num2 = 2
sum = 0
Top = 4000000
while num2 <= Top:
    if num2 % 2 == 0:
        sum += num2
    copy = num1
    num1 = num2
    num2 += copy
print(sum)
