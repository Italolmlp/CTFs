from functools import lru_cache

def check_valid_function(int_code):
    is_valid = True
    is_valid = is_valid and ((0xFF000000 & int_code) == 0xC3000000)
    is_valid = is_valid and ((0xFF0000 & int_code) == 0x580000)
    is_valid = is_valid and ((0xFF & int_code) == 0x6A)
    return is_valid

def possible_strings(data, ret_value, length = 0):
    if length == 33:
        return [""]
    possible_strings_ret = []
    possible_characters_ret_pair = []


    for index in range(ret_value * 0x100, (ret_value + 1) * 0x100):
        if index in data:
            if check_valid_function(data[index]):
                new_ret = (data[index] & 0xFF00) >> 8
                possible_characters_ret_pair.append((chr(index - ret_value * 0x100), new_ret))
    
    for p in possible_characters_ret_pair:
        possible_strings_ret += [p[0] + x for x in possible_strings(data, p[1], length+1)]
    
    return possible_strings_ret

def main():
    data = {}
    with open("data", "r") as datafile:
        for line in datafile.readlines():
            x,y = line.rstrip().split(" ")
            x = int(x, 16)
            y = int(y, 16)
            data[x] = y

    all_strings = possible_strings(data, 0x5B)
    all_strings = list(dict.fromkeys(all_strings))
    for s in all_strings:
        print(s)


if __name__ == "__main__":
    main()
