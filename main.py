# Maciej Dmowski, Jakub Strawa - ekstremalnie tania linia lotnicza
import random
import sys
import graph
import time
import generator
import argparse
import gc
from beautifultable import BeautifulTable


class UnspecifiedArgumentException(Exception):
    def __init__(self, message='Not all needed arguments are specified'):
        super(UnspecifiedArgumentException, self).__init__(message)


def write_solution_to_file(a_list, total_time_in_air, time_data, path="result.txt"):
    """
    Function writes solution of 1 problem to .txt file.

    :param a_list: solution of problem
    :param total_time_in_air: sum of all flight times
    :param time_data: full data about calculation time
    :param path: file path
    :return: None
    """
    file = open(path, "w")
    file.write(
        f"Total time in air: {total_time_in_air}\nTotal time of calculating solution: {time_data[9] - time_data[0]}\n")
    file.write('Problem generation duration ' + str(time_data[1] - time_data[0]) + '\n')
    file.write('Add vertices to graph duration ' + str(time_data[3] - time_data[2]) + '\n')
    file.write('Add edges duration ' + str(time_data[5] - time_data[4]) + '\n')
    file.write('Topological sort duration ' + str(time_data[7] - time_data[6]) + '\n')
    file.write('Path sort duration ' + str(time_data[9] - time_data[8]) + '\nFlights in order: \n')
    for elem in a_list:
        file.write("{},{}\n".format(elem[0], elem[1]))
    file.close()
    return None


def read_passed_arguments():
    """
    Function reads passed arguments and decides which mode user wants to run.

    :return: list of arguments
    """
    parser = argparse.ArgumentParser(description="generate and solve max airtime problem")
    group = parser.add_mutually_exclusive_group()
    parser.add_argument("-m", "--mode", type=int, choices=[1, 2, 3], required=True, help="choose program mode: 1, 2 or 3")
    group.add_argument("-n", "--number", type=int, help="choose how many flights to generate")
    group.add_argument("-in", "--input", type=str, help="choose input data file path")
    parser.add_argument("-out", "--output", type=str, help="choose output file path")
    parser.add_argument("-k", type=int, help="choose how many problems to generate")
    parser.add_argument("-s", "--step", type=int, help="choose step value")
    parser.add_argument("-r", type=int, default=1, help="choose how many instances of a problem to generate")
    args = parser.parse_args()

    if args.mode == 1:
        print("Mode 1")
        # read data from file and save output to file
        if args.input is None or args.output is None:
            try:
                raise UnspecifiedArgumentException()
            except UnspecifiedArgumentException as e:
                print(e)
                exit(1)
        print(f"Program will solve 1 problem from {args.input} and save it to {args.output}.")
        return [args.mode, args.input, args.output]
    elif args.mode == 2:
        print("Mode 2")
        # generating and solving 1 problem of size n
        if args.number is None or args.output is None:
            try:
                raise UnspecifiedArgumentException()
            except UnspecifiedArgumentException as e:
                print(e)
                exit(1)
        n = args.number
        if n > 10000:
            n = 10000
        print(f"Program will generate and solve 1 problem of size {n} and save it to {args.output}.")
        return [args.mode, n, args.output]
    else:
        print("Mode 3")
        # generating and solving k problems, r of same size n+k*step, in total k*r problems
        if args.number is None or args.step is None or args.k is None or args.r is None:
            try:
                raise UnspecifiedArgumentException()
            except UnspecifiedArgumentException as e:
                print(e)
                exit(1)
        n = args.number
        if n > 10000:
            n = 10000
        k = args.k
        if k <= 0:
            k = 1
        step = args.step
        while n + k * step > 10000:
            step -= 100
        if step < 0:
            step = 0
        r = args.r
        if r <= 0:
            r = 1
        print(f"Program will solve {r} instances of {k} problems with starting value of {n} with step {step}.")
        return [args.mode, k, n, step, r]


if __name__ == '__main__':

    sys.setrecursionlimit(10001)
    random.seed()
    program_parameters = read_passed_arguments()

    if program_parameters[0] == 1 or program_parameters[0] == 2:
        start = time.perf_counter()
        if program_parameters[0] == 1:
            a_list = generator.read_data_from_file(program_parameters[1])
        else:
            a_list = generator.generate_problem_data(program_parameters[1])
        end = time.perf_counter()
        time_data = [start, end]
        print('Problem generation duration ' + str(end - start))

        start = time.perf_counter()
        graph = graph.Graph(a_list)
        end = time.perf_counter()
        time_data.append(start)
        time_data.append(end)
        print('Add vertices to graph duration ' + str(end - start))

        start = time.perf_counter()
        graph.generate_edges()
        end = time.perf_counter()
        time_data.append(start)
        time_data.append(end)
        print('Add edges duration ' + str(end - start))

        start = time.perf_counter()
        graph.topological_sort()
        end = time.perf_counter()
        time_data.append(start)
        time_data.append(end)
        print('Topological sort duration ' + str(end - start))

        start = time.perf_counter()
        output = graph.max_path()
        end = time.perf_counter()
        time_data.append(start)
        time_data.append(end)
        print('Path finding duration ' + str(end - start))
        print('Total plane airtime: ' + str(output[0]))
        print('Total calculation time: ' + str(time_data[9] - time_data[0]))
        total_airtime = output[0]
        output = output[1:]
        output.reverse()
        print(output)

        if program_parameters[0] == 2:
            generator.write_data_to_file(a_list)
        write_solution_to_file(output, total_airtime, time_data, program_parameters[2])

    else:
        table = BeautifulTable(200)
        # i problems
        for i in range(program_parameters[1]):
            # j instances
            for j in range(program_parameters[4]):
                start = time.perf_counter()
                a_list = generator.generate_problem_data(program_parameters[2] + i * program_parameters[3])
                #a_list = generator.generate_special_problem_data(program_parameters[2] + i*program_parameters[3], False)
                end = time.perf_counter()
                time_data = [start, end]
                print('Problem generation duration ' + str(end - start))

                print(f"Number of flights: {len(a_list)}")
                start = time.perf_counter()
                a_graph = graph.Graph(a_list)
                end = time.perf_counter()
                time_data.append(start)
                time_data.append(end)
                print('Add vertices to graph duration ' + str(end - start))

                start = time.perf_counter()
                a_graph.generate_edges()
                end = time.perf_counter()
                time_data.append(start)
                time_data.append(end)
                print('Add edges duration ' + str(end - start))

                start = time.perf_counter()
                a_graph.topological_sort()
                end = time.perf_counter()
                time_data.append(start)
                time_data.append(end)
                print('Topological sort duration ' + str(end - start))

                start = time.perf_counter()
                output = a_graph.max_path()
                end = time.perf_counter()
                time_data.append(start)
                time_data.append(end)
                print('Path finding duration ' + str(end - start))
                print('Total plane airtime: ' + str(output[0]))
                print('Total calculation time: ' + str(time_data[9] - time_data[0]) + '\nSolution: ')
                total_airtime = output[0]
                output = output[1:]
                output.reverse()
                print(output)

                row = [program_parameters[2] + i * program_parameters[3], j + 1, total_airtime,
                       time_data[9] - time_data[0], time_data[1] - time_data[0],
                       time_data[3] - time_data[2], time_data[5] - time_data[4], time_data[7] - time_data[6],
                       time_data[9] - time_data[8], 0]
                table.rows.append(row)

                gc.collect()

            row = [program_parameters[2] + i * program_parameters[3], "average", 0, 0, 0, 0, 0, 0, 0, 0]
            for r in range(2, 9):
                avg = list(table.columns[r])
                avg = avg[-program_parameters[4]:]
                row[r] = sum(avg) / program_parameters[4]
            table.rows.append(row)

        h0 = ["Problem size", "Instance", "Tot. airtime", "Tot. calculation time", "Data generation time",
              "Add vertices time", "Add edges time", "Topological sort time", "Path finding time", "q(n)"]
        table.columns.header = h0
        table.precision = 10
        avg_rows = []
        for i in range(program_parameters[4], (program_parameters[4]+1) * program_parameters[1], program_parameters[4]+1):
            avg_rows += list(table.rows[i][0:1])
            avg_rows += list(table.rows[i][3:4])
        # calculating q(n)
        # q(n median) = 1.0, so T(n median) = t(n median)
        if len(avg_rows)/2 % 2 == 0:
            refrence_val = [avg_rows[len(avg_rows)//2], avg_rows[len(avg_rows)//2 + 1]]
        else:
            refrence_val = [avg_rows[len(avg_rows)//2 - 1], avg_rows[len(avg_rows)//2]]
        print(refrence_val)

        for r in table.rows:
            r[9] = r[3] / ((r[0]/refrence_val[0])*(r[0]/refrence_val[0])*refrence_val[1])

        print(table)
        print(table.columns[3])
        print(table.columns[9])

        file = open("table.txt", "w")
        file.write(str(table))
        file.close()
