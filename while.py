# i=0
# while i < 5 :
#     print(i)

# n=int(input("biror bir son kiriting:"))
# i=2
# while i<n:
#     if n % i == 0:
#        print("Bu natural son")
#        break
#     i+=1
# else:
#         print("Bu tub son")

while True:
    n=int(input("Natural son kiriting:"))
    if n<=0:
        print("Siz minus son kirittingiz yoki xatolik bor")
        continue
    factorial=1
    for i in range(2,n+1):
       factorial*=i
    print(f"{n}!={factorial}")