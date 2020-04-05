def hello():
    print(f'my name is {__name__} hello')


def cya():
    print(f'my name is {__name__} later')


print(f'my name is {__name__}')


if __name__ == '__main__':
    print(f'{__name__} --> hello this is main')
else:
    print(f'{__name__} is Not Main')


