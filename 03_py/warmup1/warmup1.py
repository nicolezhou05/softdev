# The parameter weekday is True if it is a weekday, and the parameter vacation
# is True if we are on vacation. We sleep in if it is not a weekday or we're on
# vacation. Return True if we sleep in.

def sleep_in(weekday, vacation):
    if weekday == False or vacation == True:
        return True
    else:
        return False
# can just be return (not weekday or vacation)

print(sleep_in(False, False)) # True
print(sleep_in(True, False)) # False
print(sleep_in(False, True)) # True


# We have two monkeys, a and b, and the parameters a_smile and b_smile indicate
# if each is smiling. We are in trouble if they are both smiling or if neither
# of them is smiling. Return True if we are in trouble.

def monkey_trouble(a_smile, b_smile):
  return(a_smile == b_smile)

print(monkey_trouble(True, True)) # True
print(monkey_trouble(False, False)) # True
print(monkey_trouble(True, False)) # False


# Given two int values, return their sum. Unless the two values are the same,
# then return double their sum.

def sum_double(a, b):
    sum = a + b
    if a == b:
        sum = sum * 2
    return sum

print(sum_double(1, 2)) # 3
print(sum_double(3, 2)) # 5
print(sum_double(2, 2)) # 8


# Given an int n, return the absolute difference between n and 21, except return
# double the absolute difference if n is over 21.

def diff21(n):
    if n <= 21:
        return 21 - n
    else:
        return (n - 21) * 2

print(diff21(19)) # 2
print(diff21(10)) # 11
print(diff21(21)) # 0


# We have a loud talking parrot. The "hour" parameter is the current hour time
# in the range 0..23. We are in trouble if the parrot is talking and the hour
# is before 7 or after 20. Return True if we are in trouble.

def parrot_trouble(talking, hour):
  return (talking and (hour < 7 or hour > 20))

print(parrot_trouble(True, 6)) # True
print(parrot_trouble(True, 7)) # False
print(parrot_trouble(False, 6)) # False


# Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.

def makes10(a, b):
  if (a == 10) or (b == 10):
    return True
  elif (a + b) == 10:
    return True
  else:
    return False
# return (a == 10 or b == 10 or a + b == 10)

print(makes10(9, 10)) # True
print(makes10(9, 9)) # False
print(makes10(1, 9)) # True


# Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num)
# computes the absolute value of a number.

def near_hundred(n):
  return (abs(100 - n) <= 10 or (abs(200 - n) <= 10))

print(near_hundred(93)) # True
print(near_hundred(90)) # True
print(near_hundred(89)) # False


# Given 2 int values, return True if one is negative and one is positive.
# Except if the parameter "negative" is True, then return True only if both are
# negative.

def pos_neg(a, b, negative):
  if negative:
    return (a < 0 and b < 0)
  else:
    return ((a < 0 and b > 0) or (a > 0 and b < 0))

print(pos_neg(1, -1, False)) # True
print(pos_neg(-1, 1, False)) # True
print(pos_neg(-4, -5, True)) # True


# Given a string, return a new string where "not " has been added to the front.
# However, if the string already begins with "not", return the string unchanged.

def not_string(str):
  if str[:3] != "not":
    str = "not " + str
  return str

print(not_string('candy')) # 'not candy'
print(not_string('x')) # 'not x'
print(not_string('not bad')) # 'not bad'


# Given a non-empty string and an int n, return a new string where the char at
# index n has been removed. The value of n will be a valid index of a char in
# the original string (i.e. n will be in the range 0..len(str)-1 inclusive).

def missing_char(str, n):
  s = str
  if n == 0:
    s = str[1:]
  elif (n == len(str) - 1):
    s = str[:(len(str) - 1)]
  else:
    s = str[:n] + str[n+1:]
  return s
# front = str[:n]
# back = str[n+1:]
# return front + back

print(missing_char('kitten', 1)) # 'ktten'
print(missing_char('kitten', 0)) # 'itten'
print(missing_char('kitten', 4)) # 'kittn'


# Given a string, return a new string where the first and last chars have
# been exchanged.

def front_back(str):
  if len(str) > 1:
    return str[len(str) - 1] + str[1:len(str) - 1] + str[0]
  else:
    return str

print(front_back('code')) # 'eodc'
print(front_back('a')) # 'a'
print(front_back('ab')) # 'ba'


# Given a string, we'll say that the front is the first 3 chars of the string.
# If the string length is less than 3, the front is whatever is there. Return a
# new string which is 3 copies of the front.

def front3(str):
  s = str
  if len(str) > 3:
    s = str[:3]
  return 3 * s

print(front3('Java')) # 'JavJavJav'
print(front3('Chocolate')) # 'ChoChoCho'
print(front3('abc')) # 'abcabcabc'
