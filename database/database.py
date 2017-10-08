# database consists of 25143 words with the longest of 22

def read_file(filename):
    with open(filename) as f:
        content = f.readlines()
        data = [x.strip() for x in content]
    return data

data = read_file('words.txt')

