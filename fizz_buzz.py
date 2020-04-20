import sys

def fizz_buzz(limit):
    for i in range(1, limit+1):
        if i % 3 ==0 and i % 5==0:
            print('fizz buzz', end=', ')
        elif i % 3 == 0:
            print('fizz', end=', ')
        elif i % 5 == 0:
            print('buzz', end=', ')
        else:
            print(i, end=', ')

def main():
    # fizz_buzz(int(sys.argv[1]))
    fizz_buzz(20)

if __name__ == '__main__':
    main()
