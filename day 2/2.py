def load_mem(first=0, second=0):
    try:
        fp = open('input.txt')
        cp_str = [int(e) for e in fp.read().split(',') ]
    finally:
        fp.close 
    cp_str[1] = first
    cp_str[2] = second
    return cp_str

def mult(a, b):
    return a * b

def add(a, b):
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

def init(first=0, second=0):
    return 0, load_mem(first, second)

def loop_computer(target):
    for x in range(0, 100):
        for y in range(0, 100):
            read_head, comp = init(x, y)
            should_quit = False
            try:
                while should_quit == False:
                    comp, read_head, should_quit = eval_computer(comp, read_head)
                if int(comp[0]) == int(target):
                    print("noun: " + str(x) + " verb: " + str(y))
                    return comp
            except CompError:
                print("err")
                raise

def main():
    target = 19690720
    comp = loop_computer(target)
    print(comp)
    return 0

main()