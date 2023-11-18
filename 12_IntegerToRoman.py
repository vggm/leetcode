
int_to_roman = {
  1: 'I',
  4: 'IV',
  5: 'V',
  9: 'IX',
  10: 'X',
  40: 'XL',
  50: 'L',
  90: 'XC',
  100: 'C',
  400: 'CD',
  500: 'D',
  900: 'CM',
  1000: 'M'
}

class Solution:
  def intToRoman(self, num: int) -> str:
    roman_number = []
    curr_number = num
    
    for n, roman in list(int_to_roman.items())[::-1]:   
      m, curr_number = curr_number // n, curr_number % n
      roman_number.append(roman * m)
 
    return ''.join(roman_number)
  
  
solution = Solution()
res = solution.intToRoman( 3 )
print(res)

solution = Solution()
res = solution.intToRoman( 58 )
print(res)

solution = Solution()
res = solution.intToRoman( 1994 )
print(res)