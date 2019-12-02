filepath = 'input'
with open(filepath) as fp:
    line = fp.readline()
    acc = 0
    cnt = 0
    while line:
        acc += int(int(line) / 3) - 2
        cnt += 1
        line = fp.readline()
    print(cnt)
    print(acc)