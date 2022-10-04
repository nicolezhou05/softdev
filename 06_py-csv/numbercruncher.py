# Joseph Wu, Purple, Nicole Zhou, Duck
# SoftDev
# K06 -- return random weighted by percentage
# 2022-10-02
# time spent: 1.5 hrs

'''
DISCO:
1) random.choice() and weight returns weighted random

QCC:
1) What are some other ways to separate occupation and percentages?

OPS SUMMARY:
1) Read the file using open() and read()
2) Use .split() to separate at '\n'
3) Separate each occupation and percentage
4) Use random.choice() and weight

'''

import random

occupation_file = open('occupations.csv', 'r')
content = occupation_file.read()

# ['occupation, percentage', 'occupation, percentage', ...]
occupation_list = content.split('\n')

# remove the trailing whitespace
occupation_list.remove('')

occupation_list.remove('Job Class,Percentage')
occupation_list.remove('Total,99.8')

# separating occupation from percentage, returns the list ['occupation', percentage]
def separate(str):
    g = str.split(',')
    # if the occupation contains a comma
    if len(g) > 2:
        i = 0
        fixed_num = len(g)
        s = ''
        while i < fixed_num - 1:
            s += g[i]
            i += 1
        g1 = []
        g1.append(s.strip())
        g1.append(float(g[-1]))
        return g1
    else:
        g[0].strip()
        g[1] = float(g[1])
        return g

ind = 0
while ind < len(occupation_list):
    occupation_list[ind] = separate(occupation_list[ind])
    ind += 1

# populating the dictionary
d = {}
index = 0
while index < len(occupation_list):
    inner_list = occupation_list[index]
    d[inner_list[0]] = inner_list[1]
    index += 1

values = list(d.values())
keys = list(d.keys())

print(random.choices(keys, weights=values))