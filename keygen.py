import random
import string

def generate_random_code():
    groups = []
    for _ in range(4):
        group = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        groups.append(group)
    return '-'.join(groups)

if __name__ == "__main__":
    print(generate_random_code())
