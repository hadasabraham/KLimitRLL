import math
import random
import os

def is_binary_str(string):
    p = set(string)
    s = {'0', '1'}
    if s == p or p == {'0'} or p == {'1'}:
        return True
    return False

def input_validation_encode_file_krll(filename, k):
    if not os.path.isfile(filename):
        raise Exception('Input file not found')
    if k < 3:
        raise Exception(f'k must be bigger than 2')
    with open("encodedFile.txt", 'w') as f_out:
        with open(filename, 'r') as f:
            for line in f.read().splitlines():
                if not is_binary_str(line):
                    raise Exception(f'all lines must be binary')

def encodeFile(filename, k = 3):
    with open("encodedFile.txt", 'w') as f_out:
        with open(filename, 'r') as f:
            for line in f.read().splitlines():
                print(encodeAnyRun(line, k), file = f_out)

def input_validation_decode_file_krll(filename, k):
    if not os.path.isfile(filename):
        raise Exception('Output file path doesn\'t exist')
    if k < 3:
        raise Exception(f'k must be bigger than 2')
    with open(filename, 'r') as f:
        for line in f.read().splitlines():
            if not is_binary_str(line):
                raise Exception(f'all lines must be binary')

def decodeFile(filename, k = 3):
    with open("decodedFile.txt", 'w') as f_out:
        with open(filename, 'r') as f:
            for line in f.read().splitlines():
                print(decodeAnyRun(line, k), file = f_out)


def input_validation_encode_any_run_krll(word, k):
    if word == "":
        raise Exception('please insert input for the algorithm')
    if k < 3:
        raise Exception(f'k must be bigger than 2')
    if not is_binary_str(word):
        raise Exception(f'word is not binary')

def encodeAnyRun(word, k = 3):
    log_n = k - 1
    n = int(math.pow(2, log_n))
    output = ''

    #cut and encode the first word
    first_word = word[: n]
    encoded_word = encodeWord(first_word)
    output += encoded_word
    last_k = encoded_word[n-k+1:]
    word = word[n:]


    #batches of n-k
    for i in range(math.floor(len(word)/(n-k))):
        small_word = last_k + word[i*(n-k): (i+1)*(n-k)]
        encoded_word = encodeWord(small_word)
        output = output[: -k] + encoded_word
        last_k = encoded_word[n-k+1:]

    last_word_len = len(word) % (n-k)
    last_word = word[-last_word_len:]

    if last_word_len == 0:
        return output
    else:
        return output[: -k] + encodeWord(last_k + last_word)


def input_validation_decode_any_run_krll(word, k):
    if word == "":
        raise Exception('please insert input for the algorithm')
    if k < 3:
        raise Exception(f'k must be bigger than 2')
    if not is_binary_str(word):
        raise Exception(f'word is not binary')


def decodeAnyRun(word, k = 3):
    #cannot be k
    #if its higher than k this means that it has been encoded
    #otherwise it has not been decoded
    output = ''
    log_n = k - 1
    n = int(math.pow(2, log_n))
    if n >= len(word):
        return decodeWord(word)
    last_word_len = (len(word) - (n + 1)) % (n - k + 1)
    if last_word_len != 0:
        decoded_last_word = decodeWord(word[-k-last_word_len:])
        left_k = decoded_last_word[: k]
        right_remainder = decoded_last_word[k:]
        output += right_remainder
        word = word[: -k-last_word_len]
        word += left_k

    while len(word) != n+1:
        last_word = word[-(n+1):]
        decoded_last_word = decodeWord(last_word)
        left_k = decoded_last_word[: k]
        right_nk = decoded_last_word[k:]
        output = right_nk + output
        word = word[: -(n+1)] + left_k

    #last block (first one) of size n+1
    return decodeWord(word) + output




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

def redundancyBits(a, b):
    return len(b) - len(a)

def checkSequence(word, k):
    zeros = '0' * k
    return zeros not in word


def generateBinaryWord(min_length, max_length):
    length = random.randint(min_length, max_length)
    word = ''
    for i in range(length):
        word += str(random.randint(0, 1))
    return word

def kLimitRLLTest(iterations = 100, min_k = 3, max_k = 10, min_length = 10, max_length = 300):
    if min_k < 3:
        return
    for i in range(iterations):
        word = generateBinaryWord(min_length, max_length)
        k = random.randint(min_k, max_k)
        encoded_word = encodeAnyRun(word, k)
        decoded_word = decodeAnyRun(encoded_word, k)
        is_it_true = decoded_word == decoded_word and checkSequence(encoded_word, k)
        if (is_it_true == False):
            print(is_it_true, word, k)

if __name__ == '__main__':
    kLimitRLLTest()
