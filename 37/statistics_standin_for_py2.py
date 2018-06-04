def mean(data):
    total = 0.0
    count = 0

    for x in data:
        total += x
        count += 1

    return total / max(1, count)