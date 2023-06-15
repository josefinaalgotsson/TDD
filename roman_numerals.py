def roman_numerals(arg):

    sum = 0
    
    arg_len = len(arg)
    add_index = 0
    for char_index in range(0,arg_len):
        use_index = char_index + add_index
        print('---------')
        print(arg)
        print(char_index)
        print(use_index)
        print(sum)
        
        if use_index == len(arg):
            return sum
        elif use_index == len(arg) - 1:
            print('here')
            sum += numeral_from_roman(arg[char_index])
            return sum
        else:
            print('there')
            this_numeral = numeral_from_roman(arg[use_index])
            next_numeral = numeral_from_roman(arg[use_index+1])
            
            if this_numeral > next_numeral or this_numeral == next_numeral: 
                sum += this_numeral
                add_index = 0
            else:
                sum += next_numeral-this_numeral
                add_index += 1
    return sum

    
def numeral_from_roman(roman):
    mapping = {"I": 1, "V": 5, "X": 10 ,"L": 50, "C": 100, "D": 500, "M": 1000}
    
    return mapping[roman]
