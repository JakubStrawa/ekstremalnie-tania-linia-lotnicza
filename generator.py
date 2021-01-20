import random

def generate_problem_data(size=10000):
    """
    Function generates list of flights of given size.

    :param size: amount of data to be generated
    :return: list with generated data
    """
    a_list = []
    for num in range(size):
        departure = random.randint(0, 29999)
        arrival = random.randint(departure + 1, 30000)
        a_list.append([departure, arrival])
    return a_list


def generate_special_problem_data(size=10000, is_short=True):
    """
    Function generates special set of data of given size :
    is_short = True, then flights have length of 1
    is_short = False, then flights have length of 30,000

    :param size: amount of data to be generated
    :param is_short: flag showing if flight should be extremely short or long
    :return: list with generated data
    """
    a_list = []
    if is_short is True:
        for num in range(size):
            departure = random.randint(0, 29999)
            a_list.append([departure, departure + 1])
    else:
        for num in range(size):
            a_list.append([0, 30000])
    return a_list


def read_data_from_file(path="data.txt"):
    """
    Function reads flights from .txt file.

    :param path: path to file with problem data
    :return: list with problem data
    """
    try:
        file = open(path, "r")
    except Exception as e:
        print(e)
        return None
    lines = file.readlines()
    a_list = []
    for line in lines:
        string = (line.replace(" ", "")).split()
        for s in string:
            if s.split(',')[0].isdecimal():
                departure = int(s.split(',')[0])
            else:
                break
            if s.split(',')[1].isdecimal():
                arrival = int(s.split(',')[1])
            else:
                break
            if departure < arrival and departure >= 0 and departure < 30000 and arrival >= 1 and arrival <= 30000:
                a_list.append([departure, arrival])
    file.close()
    return a_list


def write_data_to_file(a_list, path="generated_data.txt"):
    """
    Function writes given list to .txt file.

    :param a_list: list of flights
    :param path: file path
    :return: None
    """
    file = open(path, "w")
    for l in a_list:
        file.write("{},{}\n".format(l[0], l[1]))
    file.close()
    return None
