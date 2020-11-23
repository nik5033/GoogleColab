class Solution:
     def romanToInt(self, s: str) -> int:
     	 number = {'I': 1, 'V': 5, 'X': 10, 'L':50, 'C': 100, 'D': 500, 'M': 1000}
     	 roman = s[::-1]
     	 prev = number[roman[0]]
     	 roman = roman[1:]
     	 result = prev
     	 for a in roman:
     	 	curr = number[a]
     	 	if(curr < prev):
     	 		result -= curr
     	 	else:
     	 		result += curr
     	 	prev = curr
     	 
     	 return result
     	 	
     	 
sol = Solution()

print(sol.romanToInt(str(input("Number: "))))    	  	
