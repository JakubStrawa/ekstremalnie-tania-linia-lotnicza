import random
import sys
import graph
import time


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


def generate_problem_instances(k=10, n=100, step=50, r=1):
    """
    Function generates r instances of k problems, each problem has n+k*step flights.

    :param k: number of problems to solve
    :param n: number of generated data for 1st problem
    :param step: number of how many flights more are generated with each new problem
    :param r: number of problems of same size
    :return: list of lists with random data for problem solver
    """
    list_of_lists = []
    for i in range(k):
        for j in range(r):
            # sublist = []
            sublist = generate_problem_data(n + i * step)
            list_of_lists.append(sublist)
    return list_of_lists


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
            departure = int(s.split(',')[0])
            arrival = int(s.split(',')[1])
            if departure < arrival and departure >= 0 and departure < 30000 and arrival >= 1 and arrival <= 30000:
                a_list.append([departure, arrival])
    file.close()
    return a_list


def write_data_to_file(a_list, path="data.txt"):
    """
    Function writes given list to .txt file.

    :param a_list: list of flights
    :param path: file path
    :return: None
    """
    file = open(path, "w")
    for l in a_list:
        file.write("{},{}\n".format(l[0], l[1]))
    return None


def write_solution_to_file(a_list, total_time_in_air, total_time, path="result.txt"):
    """
    Function writes solution of 1 problem to .txt file.

    :param a_list: solution of problem
    :param total_time_in_air: sum of all flight times
    :param total_time: total calculation time
    :param path: file path
    :return: None
    """
    file = open(path, "w")
    file.write(
        "Total time in air: {}\nTotal time of calculating solution: {}\nFlights in order: \n".format(total_time_in_air,
                                                                                                     total_time))
    for l in a_list:
        file.write("{},{}\n".format(l[0], l[1]))
    return None


def read_passed_arguments():
    """
    Function reads passed arguments and decides which mode user wants to run.

    :return: list of arguments
    """
    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', str(sys.argv))
    if len(sys.argv[1]) != 3:
        print("Mod flag not included as first flag: -m<1,2,3>")
        return None
    program_mode = int(sys.argv[1][2])
    if program_mode == 2:
        # generating and solving 1 problem of size n
        n = int(sys.argv[2][2:])
        if n > 10000:
            n = 10000
        a_list = generate_problem_data(n)
        return [program_mode, a_list, n]
    elif program_mode == 3:
        # generating and solving k problems, r of same size n+k*step, in total k*r problems
        n = int(sys.argv[2][2:])
        k = int(sys.argv[3][2:])
        step = int(sys.argv[4][2:])
        r = int(sys.argv[5][2:])
        a_list = generate_problem_instances(k, n, step, r)
        return [program_mode, a_list, n, k, step, r]
    elif program_mode == 1:
        # read data from file and save output to file
        input_path = sys.argv[2]
        output_path = sys.argv[3]
        a_list = read_data_from_file(input_path)
        return [program_mode, a_list, output_path]
    else:
        print("Program mode not supported")


if __name__ == '__main__':
    sys.setrecursionlimit(10001)
    random.seed()
    # program_parameters = read_passed_arguments()
    start = time.time()
    a_list = generate_special_problem_data()
    # a_list = [[0, 3], [0, 4], [1, 8], [8, 20], [0, 35], [4, 36]]
    end = time.time()
    print('Problem generation duration ' + str(end - start))
    print(a_list)
    # a_list = generate_problem_instances(5, 2, 1, 2)
    # a_list = read_data_from_file()

    start = time.time()
    graph = graph.Graph(a_list)
    end = time.time()
    print('Add vertices to graph duration ' + str(end - start))

    start = time.time()
    graph.generate_edges()
    end = time.time()
    print('Add edges duration ' + str(end - start))

    # print(a_list)
    # print(graph)
    start = time.time()
    graph.topological_sort()
    end = time.time()
    print('Topological sort duration ' + str(end - start))
    # print(graph)

    start = time.time()
    output = graph.max_path()
    end = time.time()
    print('Path sort duration ' + str(end - start))
    print('Total airtime: ' + str(output[0]))
    output = output[1:]
    output.reverse()
    print(output)
    # print(graph)
    write_data_to_file(a_list)
    write_solution_to_file(a_list, 500, 100)
