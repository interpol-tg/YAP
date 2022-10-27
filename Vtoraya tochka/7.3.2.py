text = input()


def sort(text):
    return " ".join(map(lambda x: ''.join(sorted(list(x))), text.split()))


print(sort(text))
