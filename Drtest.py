import re

def takeSecond(elem):
    return elem[1]

def assert_executed(flag):
    global assert_flag
    assert_flag =  flag


def cite_executed(index):
    global cite_flag
    cite_flag[index] =  int(not cite_flag[index])


def raise_error():
    print("AssertError!")
    result()

def result():
    global assert_flag
    global cite_flag
    ex_method = 0
    unex_method = 0
    for i in cite_flag:
        if i == -1:
            unex_method += 1
        if i == 1:
            ex_method += 1
    print("Primitive testing: ", len(assert_loc))
    print("Helper methods: ", len(method_name))
    print("Executed Call-sites: ", ex_method)
    print("Unexecuted Call-sites: ", unex_method)
    if assert_flag == True and unex_method == 0:
        print("Green test")
    elif unex_method != 0:
        print("Rotten test")
    elif len(assert_loc) == 0:
        print("Smoke test")
    else:
        print("AssertError!")
    exit(0)


with open('test4.py','r',encoding='utf-8') as f:
    test = f.read()



assert_loc = []
assert_loc2 = []
assert_space = []
expression = []
for i in re.finditer(r'assert.*(\(.*\))', test):
    assert_loc.append(i.span())

for i in re.finditer(r'.*assert.*(\(.*\))', test):
    assert_loc2.append(i.span())
for i in range(len(assert_loc)):
    assert_space.append(assert_loc[i][0] - assert_loc2[i][0])

method_name = []
for i in range(len(assert_loc)):
    j = re.finditer(r'def(\s*).+', test[:assert_loc[i][0]])
    for k in j:
        loc = k.span()
    method_name.append(test[loc[0]+4:loc[1]-7])


while True:
    k = len(method_name)

    for i in method_name:
        new = re.finditer(r'self\.'+i, test)
        for each in new:
            loc = each.span()
        new_ = re.finditer(r'def(\s*).+', test[:loc[0]])
        for each in new_:
            loc = each.span()
        new_method_name = test[loc[0]+4:loc[1]-7]
        if new_method_name not in method_name:
            method_name.append(new_method_name)
    if k == len(method_name):
        break



for i, j in zip(reversed(assert_loc), reversed(range((len(assert_space))))):
    expression = test[i[0]+6:i[1]]
    space = ''
    for k in range(assert_space[j]):
        space = space + ' '
    new_expression = "\n" + space + "if not " + expression + ":raise_error()\n" + space + "assert_executed(True);\n"
    test = test[:i[0]] + "assert_executed(False);" +new_expression + test[i[1]:]


cite_loc = []

for i in range(len(method_name)):
    for j in re.finditer("\S.+\."+method_name[i]+".+", test):
        cite_loc.append(j.span())
cite_loc.sort(key=takeSecond, reverse=True)


cite_flag = [-1 for i in range(len(cite_loc))]


for i,j in zip(cite_loc, range(len(cite_loc))):
    test = test[:i[0]] + "cite_executed(%s);"%j + test[i[0]:i[1]] + ";cite_executed(%s)"%j + test[i[1]:]



# exec(test)
#
#
# result()
# print(test)









