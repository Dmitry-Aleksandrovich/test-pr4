# data_validator.py
def validate_data(input_data):
    """
    Проверяет корректность входных данных.
    
    :param input_data: список данных
    :return: True, если все элементы — целые числа; иначе False
    """
    return all(isinstance(x, int) for x in input_data)

