def checkio(data):
    data = sorted(data)
    l = len(data)
    if l % 2:
        return data[l // 2]
    else:
        return (data[l // 2] + data[l // 2 - 1]) / 2
