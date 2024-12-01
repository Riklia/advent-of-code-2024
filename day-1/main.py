from collections import Counter

if __name__ == "__main__":
    data = [[], []]
    with open("input.txt") as file:
        for line in file:
            row = line.strip().split()
            data[0].append(int(row[0]))
            data[1].append(int(row[1]))

    left_list_sorted = sorted(data[0])
    right_list_sorted = sorted(data[1])

    part_1_answer = sum(abs(left - right) for left, right in zip(left_list_sorted, right_list_sorted))
    print("Part 1: ", part_1_answer)

    right_counter = Counter(data[1])
    similarity_score = sum(num * right_counter[num] for num in data[0])
    print("Part 2: ", similarity_score)
