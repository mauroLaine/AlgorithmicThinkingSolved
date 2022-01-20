def find_identical_snow_flake(snow_flakes):
    if find_identical(snow_flakes):
        print("Twin snowflakes found")
    else:
        print("No twin snowflakes are alike")


def find_identical(snow):
    for i in range(0, len(snow)):
        for j in range(i + 1, len(snow)):
            if are_identical(snow[i], snow[j]):
                return True
    return False


def are_identical(snow1, snow2):
    for i in range(0, len(snow1)):
        if find_right_identical(snow1, snow2, i):
            return True
        elif find_left_identical(snow1, snow2, i):
            return True
    return False


def find_right_identical(snow1, snow2, start):
    for offset in range(0, len(snow1)):
        snow2_index = (offset + start) % len(snow1)
        # print(str(snow1[offset]) + ", " + str(snow2[snow2_index]))
        if snow1[offset] != snow2[snow2_index]:
            return False
    return True


def find_left_identical(snow1, snow2, start):
    for offset in range(0, len(snow1)):
        snow2_index = start - offset
        if snow2_index < 0:
            snow2_index = snow2_index + len(snow1)
        # print(str(snow1[offset]) + ", " + str(snow2[snow2_index]))
        if snow1[offset] != snow2[snow2_index]:
            return False
    return True


if __name__ == "__main__":
    n = int(input())
    snow_flakes = [0] * n
    print(snow_flakes)
    for i in range(0, len(snow_flakes)):
        values = input()
        values = values.split(" ")
        snow_flakes[i] = list(map(int, values))
    print(snow_flakes)
    find_identical_snow_flake(snow_flakes)
