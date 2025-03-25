# num = int(input("Please enter a number: "))
# is_prime = True

# for i in range(2, int(num ** 0.5)):
#     if num % i == 0:
#         is_prime = False
#         break
# print(is_prime)

num = int(input("Please enter a number: "))
count = 0

for i in range(2, (num // 2) + 1):
    if num % i == 0:
        count = count + 1
if count == 0:
    print("Number is prime")
        
else:
        print("The number is not prime")


