
def is_string(s):
    """Returns true if s is a string and false otherwise"""
    return type(s) == str

testcases = ["hello", ["hello"], " This is a long sentence!"]

for test in testcases:
    print("Is {} a string? {}".format(test,is_string(test)))
