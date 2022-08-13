import sys

from models import Value, Addition, Subtraction


def main():
    val1 = Value(1)
    val2 = Value(2)
    sum = Subtraction(val1, val2)
    sum.print_myself(sys.stdout)
    print()
    sum.evaluate({}).print_myself(sys.stdout)


if __name__ == "__main__":
    main()
