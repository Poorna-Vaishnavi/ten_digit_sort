def ten_digit_sort():
    b=sorted(a,key=lambda x:((x//10)%10,-x))
    return b
a=list(map(int,input().split()))
print(ten_digit_sort())