
def delete():
    A = list(map(int,input('Enter a list: ').split()))
    print("Оригінальний список:", A)
    value = int(input('Введіть значення для видалення: '))
    result = []
    for x in A:
        if x != value:
            result.append(x)
    print("Оновлений список:", result)
    return result
delete()
