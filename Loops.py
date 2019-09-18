guess = 1                       # to rename a variable, go to variable, right click, refactor, rename
# while guess <= 5:
#   print(guess)                # print("Value:"+ i) will not work
#   print('*' * guess)
#    guess = guess + 1                 # i++ will not work

secret_number = 9
maximum_attempt = 3
count = 0
while count < maximum_attempt:
    num = input('Number:')
    # print(num)
    count = count + 1
    if int(num) == secret_number:       # if num == secret_number will not work
        print('You Win!!!')
        break
    else:
        print("Try Again")
