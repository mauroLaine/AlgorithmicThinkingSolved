def food_lines(n, m, lines):
    print("--- Initial lines: " + str(lines))
    for i in range(1, m + 1):
        index = find_shortest_line(lines)
        lines[index] = lines[index] + 1
        line_joined = index + 1
        print(line_joined)
    print("--- Final lines: " + str(lines))


def find_shortest_line(lines):
    index = 0
    for i in range(0, len(lines)):
        if lines[i] < lines[index]:
            index = i
    return index


if __name__ == "__main__":
    print("Food Lines \n")
    n, m = input().split()
    n = int(n)
    m = int(m)
    lines = [0] * n
    p = input().split()
    for i in range(0, len(p)):
        lines[i] = int(p[i])
    food_lines(n, m, lines)
