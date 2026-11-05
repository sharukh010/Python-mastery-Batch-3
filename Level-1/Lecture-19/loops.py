"""
for loop - it is based on sequence of items 
ex: 
eating - it is a task 
cookies - it is the items (count is fixed)
lets assume a packet has 9 cookies so we perform eating operation (task) on 
one cookie at a time (like this we will implement it on all the cookies)
sequences / iteratables : list,tuple,dictionary,set, range 

while loop
ex: 
packing - it is a task 
cookeis - it is the item (count is not fixed)
- we will perform the packing until no cookies let 
- it is based on condition 
"""
# nums = [10,20,30,40,50]
# # find the sum of all the elements in the list 
# total = 0 
# for num in nums: 
#     total += num 

# print(f"Total: {total}")

# take numbers from user one at a time continue until he enters 0 and find the sum of all the elements that he has entered 

# num = -1 
# total = 0 
# while num != 0 : 
#     num = int(input("Number: "))
#     total += num 
# print(f"Total: {total}")

# continue will skip current iteration / item in the loop 
# break will stop the whole loop

# you need to take one number at a time from user and you need to add it only when the number is positive and you need to skip negative numbers and whenever user enters 0 you need to stop 

"""
control statements: 
1. break - breaks a loop 
2. continue - skip a loop iteration 
3. return - return from function execution 
"""
num = -1 
total = 0 
while True: 
    num = int(input("Number: "))
    if num > 0: 
        total += num 
        print("Adding number to total")
    elif num == 0: 
        print("Breaking the loop..")
        break # it breaks the loop
        # print("this is also not reachable")
    else: 
        print("Skipping the number")
        continue # it skips negative numbers 
        # print("hello") # this is unreachable 
    # anything below this line inside the loop will be ignored when 
    # you hit continue 
print(f"Total: {total}")