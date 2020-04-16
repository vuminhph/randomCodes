def sumDigits(num):
  while len(str(num)) != 1:
    num = sum([int(char) for char in str(num)])
  return num

print(sumDigits(439230))