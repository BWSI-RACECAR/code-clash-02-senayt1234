"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2023

Code Clash #2 - Digit Decrypt (digitdecrypt.py)


Author: Koneshka Bandyopadhyay

Difficulty Level: 4/10

Prompt: Koneshka has a collection of 9 RACECARS, each with unique speed and a crypted 
identification number that helps identify the rankings of each of the RACECARS in terms
of speed. Write a program that helps identify the ranking of a car given the identification
number. The way we can decrypt this identification number is by adding digits of the number 
until we reach single digits. For example: Let’s say that the identification number is 38. 
Then, we add ‘3’ + ‘8’ to get 11. We further add the digits ‘1’+ ‘1’ to get 2, ranking the car
in 2nd place or 2nd fastest out of 9. Car with identification 1111 gives us 1+1+1+1=4, ranking 
the car 4th fastest out of 9. The goal is to add the digits until we reach single digits.

Test Cases:
Input: 48 Output: 3

Input: 13 Output: 4

Input: 0 Output: 0 
"""

class Solution:    
    def digitdecrypt(self, num):
            #type num: int
            #return type: int
            if num == 0:
               return 0
            if num<10:
               return num
            if num<0:
               return "place a postive interger"
            num = str(num)
            index = 0
            total = 0
            while len(num)>index:
                total = int(num[index])+total
                index = index +1
            total = str(total)
            fun = 0
            index = 0 
            while len(total)>index:
                fun = int(total[index])+fun
                index = index +1
            return fun
            
 
def main():
    input1= input()
    input2 = int(input1)

    
    tc1 = Solution()
    ans = tc1.digitdecrypt(input2)
    print(ans)
    
if __name__ == "__main__":
    main()