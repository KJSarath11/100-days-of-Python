#even odd
target=int(input())#100
even_sum=0
for number in range(2,target+1,2):
    even_sum+=number
print(f"Even sum={even_sum}")