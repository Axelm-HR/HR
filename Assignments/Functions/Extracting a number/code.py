def extract_first_number_from_string(s1):
    for i in s1.split():
        if i.isnumeric():
            return int(i)
    return -1

