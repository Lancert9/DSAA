def move(n, src, dest, temp):
    if n >= 1:
        move(n - 1, src, temp, dest)
        print "Move %d -> %d" % (src, dest)
        move(n - 1, temp, dest, src)

if __name__ == '__main__':
    move(5, 1, 3, 2)

