
def is_string(s):
    """Returns true if s is a string and false otherwise"""
    return type(s) == str

def is_only_string(s):
    """Returns true if s is a string that contains no spaces or digits"""
    if not is_string(s):
        return False
    forbidden = [" "];
    for i in range(0,10):
        forbidden += str(i);
    return not any(el in s for el in forbidden)


is_string_testcases = ["hello", ["hello"], " This is a long sentence!"]
is_only_string_testcases = ["11", "hello", "This is a long sentence!"]

for test in is_string_testcases:
    print("Is {} a string? {}".format(test,is_string(test)))

for test in is_only_string_testcases:
    print("Is {} a string? {}".format(test,is_only_string(test)))
