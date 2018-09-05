'''
4. Write a program that prints the name Fred 100 times, one time per line.
'''


def zero_to_num(name,c=100):
    for i in range(c):
        print(name)

if __name__ == '__main__':
    name = 'Fred'
    zero_to_num(name,10)
