# Задача 3
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример:
# На сжатие:
# Входные данные:
# WWWWWWwwwwwwwBaaaaaaaWWWWWWBBBWWWWWWWWWWWWWwwwwwwwBWWWWWWWWcccccccccc
# Входные данные:
# 12W1B12W3B24W1B14W

with open('task_3_RLE_decoded.txt', 'r') as data:
    my_File = data.read()

def rle_encode(data):
    encoding = '' 
    prev_char = ''
    count = 1 
    if not data: return ''
    for char in data: 
        if char != prev_char:
            if prev_char: 
                encoding += str(count) + prev_char 
            count = 1 
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char 
        return encoding
        
print()
encoding = rle_encode(my_File)
print(f'{encoding}\n')


with open('task_3_RLE_encoded.txt', 'r') as data:
    my_File2 = data.read()

def rle_decode(data): 
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char 
        else:
            decode += char * int(count)
            count = '' 
    return decode


decode = rle_decode(my_File2)
print(f'{decode}\n')