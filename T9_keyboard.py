
types = {
  '2': 'ABC',
  '3': 'DEF',
  '4': 'GHI',
  '5': 'JKL',
  '6': 'MNO',
  '7': 'PQRS',
  '8': 'TUV',
  '9': 'WXYZ',
  '0': ' '
}

class Solution:
  def T9_keyboard(text: str) -> str:
    
    message = ''
    
    for numbers in text.split('-'):
      digit = numbers[0]
      message += types[digit][len(numbers)-1]
    
    return message

  def T9_keyboard2(text: str) -> str:
    return ''.join(types[numbers[0]][len(numbers)-1] for numbers in text.split('-'))

text = input()
print(Solution.T9_keyboard2(text))