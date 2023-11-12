#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = len(sys.argv) - 1
    sum = 0

    # Convert arguments to integers and sum
    for m in range(1, args + 1):
        num = int(sys.argv[m])
        if (num <= 0 or num >= 0):
            sum = sum + num
        else:
            continue
        print("{}".format(sum))
