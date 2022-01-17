def up_to_3_digits_as_int(str_num):
    below_20 = {
                "eleven": 11,
                "twelve": 12,
                "thirteen": 13,
                "fourteen": 14,
                "fifteen": 15,
                "sixteen": 16,
                "seventeen": 17,
                "eighteen": 18,
                "nineteen": 19  ,                       
                "one": 1,
                "two": 2,
                "three": 3,
                "four": 4,
                "five": 5,
                "six": 6,
                "seven": 7, 
                "eight": 8,
                "nine": 9,
                "ten": 10
             }
    tens = {
                "twenty": 20,
                "thirty": 30,
                "forty": 40,
                "fifty": 50,
                "sixty": 60,
                "seventy": 70,
                "eighty": 80,
                "ninety": 90
            }
    num = 0
    if "hundred" in str_num:
        k = str_num.index("hundred")
        num = below_20[str_num[:k-1]]*100
        str_num = str_num[k+7:]
    for element in tens:
        if element in str_num:
            num += tens[element]
            str_num = str_num.replace(element, "")
            break
    for element in below_20:
        if element in str_num:
            num += below_20[element]
            break
    return num

def parse_int(string):
    if "million" in string:
        return 10**6
    number = 0
    if "thousand" in string:
        i = string.index("thousand")
        thousands = string[:i]
        number = up_to_3_digits_as_int(thousands) * 10**3
        string = string[i+9:]
    number += up_to_3_digits_as_int(string)
    return number



for element in ["one million", "seventy-two","sixty-eight", "nineteen", "seven hundred eighty-three thousand nine hundred and nineteen"]:
    print(parse_int(element))
