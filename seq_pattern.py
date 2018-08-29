import random

def generate_pattern1():
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

def generate_pattern2():
    fi = open("save/real_data.txt", "w")
    random.seed(100)
    for i in range(9984):
        index = random.randint(1, 100)
        line = [0] * 20
        for i in range(20):
            line[i] = random.randint(500, 2000)
        pos = random.randint(0, 7)
        for i in range(pos, pos + 3):
            line[i] = index
        pos = random.randint(10, 17):
        for i in range(pos, pos + 3):
            line[i] = index + 2
        fi.write(" ".join(line) + "\n")
    fi.close()

# cycle
def generate_pattern3():
    fi = open("save/real_data.txt", "w")
    random.seed(100)
    for i in range(9984):
        index = random.randint(1, 100)
        line = [0] * 20
        for i in range(20):
            line[i] = random.randint(500, 2000)
        pos = random.randint(0, 7)
        cycle = random.randint(2, 5)
        for i in range(100):
            pp = pos + i * cycle
            if pp <= 20:
                line[pp] = index
        fi.write(" ".join(line) + "\n")
    fi.close()


if __name__ == '__main__':
    generate_pattern3()