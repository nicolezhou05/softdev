# Given a string and a non-negative int n, return a larger string that is n
# copies of the original string.

def string_times(str, n):
  return str * n

print(string_times('Hi', 2)) # 'HiHi'
print(string_times('Hi', 3)) # 'HiHiHi'
print(string_times('Hi', 1)) # 'Hi'


#  Given a string and a non-negative int n, we'll say that the front of the
# string is the first 3 chars, or whatever is there if the string is less than
# length 3. Return n copies of the front;

def front_times(str, n):
  front = ""
  if len(str) < 3:
    front = str
  else:
    front = str[:3]
  return n * front

print(front_times('Chocolate', 2)) # 'ChoCho'
print(front_times('Chocolate', 3)) # 'ChoChoCho'
print(front_times('Abc', 3)) # 'AbcAbcAbc'


# Given a string, return a new string made of every other char starting with
# the first, so "Hello" yields "Hlo".

def string_bits(str):
  return str[::2]

print(string_bits('Hello')) # 'Hlo'
print(string_bits('Hi')) # 'H'
print(string_bits('Heeololeo')) # 'Hello'


# Given a non-empty string like "Code" return a string like "CCoCodCode".

def string_splosion(str):
  s = ""
  x = 1
  while x < len(str) + 1:
    s += str[:x]
    x += 1
  return s

print(string_splosion('Code')) # 'CCoCodCode'
print(string_splosion('abc')) # 'aababc'
print(string_splosion('ab')) # 'aab'


# Given a string, return the count of the number of times that a substring
# length 2 appears in the string and also as the last 2 chars of the string,
# so "hixxxhi" yields 1 (we won't count the end substring).

def last2(str):
  i = 0
  count = 0
  while i < len(str) - 2:
    if (str[i] == str[len(str) - 2]) and (str[i + 1] == str[len(str) - 1]):
      count += 1
    i += 1
  return count

print(last2('hixxhi')) # 1
print(last2('xaxxaxaxx')) # 1
print(last2('axxxaaxx')) # 2


# Given an array of ints, return the number of 9's in the array.

def array_count9(nums):
  count = 0
  for x in nums:
    if x == 9:
      count += 1
  return count

print(array_count9([1, 2, 9])) # 1
print(array_count9([1, 9, 9])) # 2
print(array_count9([1, 9, 9, 3, 9])) # 3


# Given an array of ints, return True if one of the first 4 elements in the
# array is a 9. The array length may be less than 4.

def array_front9(nums):
  limit = 4
  i = 0
  if len(nums) < 4:
    limit = len(nums)
  while i < limit:
    if nums[i] == 9:
      return True
    i += 1
  return False

print(array_front9([1, 2, 9, 3, 4])) # True
print(array_front9([1, 2, 3, 4, 9])) # False
print(array_front9([1, 2, 3, 4, 5])) # False


# Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears
# in the array somewhere.

def array123(nums):
  i = 0
  while i < len(nums) - 1:
    if nums[i:i+3] == [1, 2, 3]:
      return True
    i += 1
  return False

print(array123([1, 1, 2, 3, 1])) # True
print(array123([1, 1, 2, 4, 1])) # False
print(array123([1, 1, 2, 1, 2, 3])) # True


# Given 2 strings, a and b, return the number of the positions where they
# contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since
# the "xx", "aa", and "az" substrings appear in the same place in both strings.

def string_match(a, b):
  count = 0
  i = 0
  while i < len(a) - 1:
    if a[i:i+2] == b[i:i+2]:
      count += 1
    i += 1
  return count

print(string_match('xxcaazz', 'xxbaaz')) # 3
print(string_match('abc', 'abc')) # 2
print(string_match('abc', 'axc')) # 0
