def load_computer():
    try:
        fp = open('input.txt')
        cp_str = [int(e) for e in fp.read().split(',') ]
    finally:
        fp.close 
    return cp_str

def mult(a, b):
    return a * b

def add(a, b):
    print(a + b)
    return a + b

def getVal(comp, a):
    return comp[comp[a]]

def doCalc(a, b, fn):
    return fn(a, b)

def writeTo(computer, val, target):
    computer[target] = val
    return computer

def evalCmd(computer, rh, fn):
    return writeTo(computer, doCalc(getVal(computer, rh + 1), getVal(computer, rh + 2), fn), computer[rh + 3])


def eval_computer(computer, rh):
    command = computer[rh]
    if command == 99:
        return computer, rh, True
    elif command == 1:
        return evalCmd(computer, rh, add), rh + 4, False
    elif command == 2:
        return evalCmd(computer, rh, mult), rh + 4, False
    else:
        raise CompError(computer, "Invalid state at: " + rh)

class CompError(Exception):
    def __init__(self, computer, message):
        self.computer = computer
        self.message = message

def main():
    comp = load_computer()
    read_head = 0
    should_quit = False
    try:
        while should_quit == False:
            comp, read_head, should_quit = eval_computer(comp, read_head)
            print(comp)
            print(read_head)
    except CompError:
        raise
main()