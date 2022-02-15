import math


def encodeFile(filename, k = -1):
    with open("encodedFile.txt", 'w') as f_out:
        with open(filename, 'r') as f:
            for line in f.read().splitlines():
                print(encodeAnyRun(line, k), file = f_out)


def decodeFile(filename, k = -1):
    with open("decodedFile.txt", 'w') as f_out:
        with open(filename, 'r') as f:
            for line in f.read().splitlines():
                print(decodeAnyRun(line, k), file = f_out)



def encodeAnyRun(word, k = -1):
    if k == -1:
        return encodeWord(word)
    log_n = k - 1
    n = int(math.pow(2, log_n))
    output = ''
    for i in range(math.floor(len(word)/n)):
        small_word = word[i*n: (i+1)*n]
        output += encodeWord(small_word)

    last_word_len = len(word) % n
    last_word = word[-last_word_len:]
    if last_word_len < k:
        return output + last_word
    else:
        return output + encodeWord(last_word)

def decodeAnyRun(word, k = -1):
    if k == -1:
        return decodeWord(word)
    log_n = k - 1
    n = int(math.pow(2, log_n))
    output = ''
    for i in range(math.floor(len(word)/(n+1))):
        small_word = word[i*(n+1): (i+1)*(n+1)]
        output += decodeWord(small_word)

    last_word_len = len(word) % (n+1)
    last_word = word[-last_word_len:]
    if last_word_len < k:
        return output + last_word
    else:
        return output + decodeWord(last_word)




def decodeWord(word):
    length = len(word)
    k = math.ceil(math.log(length - 1, 2)) + 1
    zeros = '0' * k
    while word[length - 1] != '1':
        word = word[: length - 1]
        binary_index = word[length - k:]
        index = int(binary_index, 2) - 1
        word = word[: length - k]
        before_word = word[: index]
        after_word = word[index:]
        word = before_word + zeros + after_word
    word = word[: length - 1]
    return word


def encodeWord(word):
    length = len(word)
    k = math.ceil(math.log(length, 2)) + 1
    zeros = '0' * k
    y = word + '1'
    i = 0
    i_end = length - k
    while i <= i_end:
        block = y[i: i + k]
        if block == zeros:
            i_plus = i + 1
            binary_index = f"{i_plus:0{k-1}b}"
            y_before = y[0: i]
            y_after = y[i+k:]
            y = y_before + y_after + binary_index + '0'
            i_end -= k
        else:
            i += 1
    return y



if __name__ == '__main__':
    encodeFile('b.txt')
    decodeFile('encodedFile.txt')
