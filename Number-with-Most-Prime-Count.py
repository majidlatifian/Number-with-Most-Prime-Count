prime_final = 0
answer = 0

for i in range(0,10):
    number = int(input())
    prime = 0
    
    
    for j in range(2,number+1):
        counter = 0
        if number % j == 0:
            for k in range(2,j):
                if j % k == 0:
                    counter += 1
            if counter == 0:
                prime += 1
    if prime > prime_final:
        prime_final = prime
        answer = number
    if prime == prime_final:
        if number > answer:
            answer = number



print (answer, prime_final)

