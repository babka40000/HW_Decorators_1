from debug import decorator


@decorator('log1.txt')
def test(x, y):
    return x * y


if __name__ == '__main__':
    print(test(3, 5))
