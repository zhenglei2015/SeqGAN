import random

def generate_pattern():
    fi = open("save/real_data.txt", "w")
    random.seed(100)
    for i in range(9984):
        index = random.randint(1, 100)
        line = range(20)
        pos = []
        for k in range(4):
            pos.append(random.randint(k * 5, (k + 1) * 5))
        nextPos = 0
        for k in range(20):
            if k != pos[nextPos]:
                line[k] = str(random.randint(500, 2000))
            elif pos[nextPos] < 15:
                line[k] = str(index)
                nextPos = nextPos + 1
            else:
                line[k] = str(index + 2)
        fi.write(" ".join(line) + "\n")
    fi.close()


if __name__ == '__main__':
    generate_pattern()