import numpy as np


def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): _description_. Defaults to 1.

    Returns:
        int: _description_
    """
    
    count = 0
    first = 1
    last = 101
    predict_number = (first + last)//2
    
    while number != predict_number:
        count += 1
        if predict_number > number:
            last = predict_number
        elif predict_number < number:
            first = predict_number
        predict_number = (first + last)//2

    return count

print(f'Количество попыток: {random_predict()}')


def score_game(random_predict) -> int:
    count_ls = []
    random_array = np.random.randint(1, 101, size=(1000))
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

if __name__ == '__main__':
    score_game(random_predict)