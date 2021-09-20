
def add_2_list():
    li = []
    while True:
        num = input('enter number: ')
        if isinstance(num, int):
            li.append(num)
            print(li)
            continue
        if num == 'done':
            print(li)
            break

add_2_list()

