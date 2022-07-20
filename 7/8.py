#8

def sort(string):
    if string[0] == '0':
        return ""
    else:
        if int(string[0]) < 0:
            return f"{int(string[0])} {sort(string[1:])}"
        else:
            return f"{sort(string[1:])} {int(string[0])}"


with open('input2.txt', 'r') as input_data:
    with open('output2.txt', 'w') as output:
        output.write(sort(input_data.read().split(" ")))
