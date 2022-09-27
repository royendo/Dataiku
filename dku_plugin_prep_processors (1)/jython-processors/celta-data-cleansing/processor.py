trim_column = params.get('trim_column')
input_columns= params.get('input_columns')
add_flag_column = params.get('add_flag_column')
flag_name = params.get('flag_name')

def process(row):

    for input_column in input_columns:
        VALUE = row[input_column]
        if VALUE is not None:
            VALUE = VALUE.encode("latin", "ignore")
            VALUE = ''.join([' ' if ord(i) in [9, 10, 11, 12, 13, 28, 29, 30, 31, 32, 133, 160] else i for i in VALUE ]) # Clean special characters that are whitespace

            if trim_column:
                VALUE = VALUE.strip()
            
            if add_flag_column:
                row[flag_name] = row[input_column] != VALUE
                
                
        row[input_column] = VALUE

    return row
