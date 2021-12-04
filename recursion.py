
i = [0, 1]

def fibonacci(leng):

    if len(i) == leng:
        print("DONE")
        return False
    else:
        num = i[-1] + i[-2] 
        i.append(num)
        print(num)
        fibonacci(leng)
    print(i)


if __name__ == '__main__':
    fibonacci(12)