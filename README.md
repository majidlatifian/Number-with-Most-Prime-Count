# Number-with-Most-Prime-Count
This Python script calculates the number with the highest count of prime numbers from a series of user inputs. It prompts the user to enter 10 numbers and determines which number has the most primes. The script then displays the number and the count of prime numbers.

## Prerequisites
Python 3.x
## How to use
1. Run the script in a Python environment.
2. Enter 10 integer numbers when prompted by the script.
3. The script will calculate the count of prime numbers for each input and determine the number with the highest count.
4. Finally, the script will display the number and the count of prime numbers.
## Code Explanation
1. The script defines a function is_prime(n) to check if a number n is prime. It utilizes an efficient prime checking algorithm.
2. The function find_number_with_most_primes() encapsulates the main logic. It iterates through the user inputs, counts the prime numbers for each input, and keeps track of the number with the highest count.
3. The script uses the is_prime() function to determine the count of prime numbers for each input.
4. After processing all inputs, the script prints the number with the highest count of prime numbers.

## Example
```
Enter 10 numbers:
23
12
37
45
2
17
10
9
31
6

Output:
Number with Most Primes: 37
Count of Primes: 2
```
In this example, the number 37 has the highest count of prime numbers, which is 2.

