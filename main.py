import sys

from models import Value, Addition, Subtraction


def main():
    val1 = Value(1)
    val2 = Value(2)
    sum = Subtraction(val1, val2)
    print(sum)
    print()
    print(sum.evaluate({}))


if __name__ == "__main__":
    main()
