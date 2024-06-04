end_number = 20

for num in range(1, end_number+1) :
    if num % 3 == 0 :
        print('fizz', end=' ')
    else :
        print(num, end=' ')