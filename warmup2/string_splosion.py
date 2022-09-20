# Given a non-empty string like "Code" return a string like "CCoCodCode".

def string_splosion(str):
  s = ""
  x = 1
  while x < len(str) + 1:
    s += str[:x]
    x += 1
  return s

string_splosion('Code') # 'CCoCodCode'
string_splosion('abc') # 'aababc'
string_splosion('ab') # 'aab'
