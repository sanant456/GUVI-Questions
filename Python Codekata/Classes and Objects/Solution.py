class RemainderCalculator:
  def __init__(self, n, k, a):
    self.n = n
    self.k = k
    self.a = a

def calculate_remainders(self):
  rem = {}
  #.... YOUR CODE STARTS HERE ....
  for num in self.a:
            remainder = num%self.k
            if remainder!=0:
                rem[remainder]=rem.get(remainder,0)+1
  #.... YOUR CODE ENDS HERE ....

 return rem

def find_maximum_result(self, num):
  #.... YOUR CODE STARTS HERE ....

  result =0
        for r, count in rem.items():
            moves =(self.k * (count - 1)) + (self.k - r)+1
            result = max(result,moves)
        return result
    #.... YOUR CODE ENDS HERE ....

if __name__ = "__main__":
from sys import stdin, stdout, setrecursionlimit
