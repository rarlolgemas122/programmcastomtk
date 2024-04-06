# модуль visual.py будет отвечать за отрисовку gui, logic.py - за логику: высчитывание ответа

def op_1(input_data):
    number = int(input_data)
    result_number = number * 2
    output_data = str(result_number)
    return output_data


def op_2(input_data):
    number = int(input_data)
    result_number = number + 5
    output_data = str(result_number)
    return output_data
