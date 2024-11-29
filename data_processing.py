# data_processing.py
def process_data(input_data):
    """
    Обрабатывает входные данные, возводя положительные числа в квадрат.
    
    :param input_data: список чисел
    :return: список квадратов положительных чисел
    """
    return [x**2 for x in input_data if x > 0]

