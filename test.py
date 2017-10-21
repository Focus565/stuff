"""GCD"""
def main():
    """find gcd"""
    num1 = int(input())
    num2 = int(input())
    num1, num2 = max(num1, num2), min(num1, num2)
    if num2 == 0:
        ans = 0
    for i in range(num2, 0, -1):
        if num1%i == 0 and num2%i == 0:
            print(i)
            print(890)
main()
