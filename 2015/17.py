import read_input


def solve1(input) -> None:
    n = len(input)
    count = 0
    for b in range(2**n):
        bits = [int(d) for d in f'{b:020b}']
        total = sum([used * capacity for (used, capacity) in zip(bits, input)])
        if total == 150:
            count += 1
    print(count)


def solve2(input) -> None:
    n = len(input)
    counts = {}
    for b in range(2**n):
        bits = [int(d) for d in f'{b:020b}']
        total = sum([used * capacity for (used, capacity) in zip(bits, input)])
        if total == 150:
            container_count = sum(bits)
            if container_count not in counts:
                counts[container_count] = 0

            counts[container_count] += 1
    print(counts[min(counts.keys())])


if __name__ == '__main__':
    input = read_input.numbers()
    # print(input)
    solve1(input)
    solve2(input)
