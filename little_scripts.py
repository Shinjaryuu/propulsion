
def is_string(s):
    """Returns true if s is a string and false otherwise"""
    return type(s) == str

def test_is_string():
    testcases = ["hello", ["hello"], " This is a long sentence!"]
    results = [True, False, True]
    return all(is_string(t)==r for (t,r) in zip(testcases,results))

def is_only_string(s):
    """Returns true if s is a string that contains no spaces or digits"""
    if not is_string(s):
        return False
    forbidden = [" "];
    for i in range(0,10):
        forbidden += str(i);
    return not any(el in s for el in forbidden)

def test_is_only_string():
    testcases = ["11", "hello", "This is a long sentence!"]
    results = [False, True, False]
    return all(is_only_string(t)==r for (t,r) in zip(testcases,results))

def is_alphanumeric(s):
    if not is_string(s):
        return False
    return s.isalnum()

def test_is_alphanumeric():
    testcases = ["11",["hello"],"this is a long sentence","this is a string...!!!"]
    results = [True, False, False, False]
    return all(is_alphanumeric(t)==r for (t,r) in zip(testcases,results))

def are_same_type(l):
    """Returns true if all elements of the list are the same type"""
    return all(type(el)==type(l[0]) for el in l)

def test_are_same_type():
    testcases = [["hello","world","long sentence"],
                                [1,2,9,10],
                                [1,2,9,"hello"]]
    results = [True,True,False]
    return all(are_same_type(t)==r for (t,r) in zip(testcases,results))

def intersection(a,b):
    """Returns a sorted list of all the letters contained at least once in a or b"""
    return "".join(sorted(set(c for c in a+b)))

def test_intersection():
    a = "xyaabbbccccdefww"
    b = "xxxxyyyyabklmopq"
    x = "abcdefghijklmnopqrstuvwxyz"
    return (intersection(a,b)=="abcdefklmopqwxy")& (intersection(a,x)=="abcdefghijklmnopqrstuvwxyz")

def convert(n):
    """returns reverse sorted list of digits of the number"""
    return sorted((int(c) for c in str(n)),reverse=True)

def test_convert():
        testcases = [429563, 324]
        results = [[9,6,5,4,3,2],[4,3,2]]
        return all(convert(t)==r for (t,r) in zip(testcases,results))


print("Testing is_string(): {}".format(test_is_string()))
print("Testing is_only_string(): {}".format(test_is_only_string()))
print("Testing is_alphanumerc(): {}".format(test_is_alphanumeric()))
print("Testing are_same_type(): {}".format(test_are_same_type()))
print("Testing intersection(): {}".format(test_intersection()))
print("Testing convert(): {}".format(test_convert()))
