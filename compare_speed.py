import numpy as np
import pyarrow as pa
import pandas as pd
import pyarrow.compute as pc
import matplotlib.pyplot as plt
import time

def time_loop(integers1, integers2):
    start = time.time()
    integers3 = []
    for i, int1 in enumerate(integers1):
        integers3.append(int1 * integers2[i])
    return time.time() - start

def time_numpy(integers1, integers2):
    start = time.time()
    integers3 = np.multiply(integers1, integers2)
    return time.time() - start

def time_pyarrow(table):
    start = time.time()
    integers3 = pc.multiply(table.column("integer_1"), table.column("integer_2"))
    return time.time() - start

def visualize_times(integers1, integers2, table):
    plt.clf()
    times = [time_loop(integers1, integers2), time_numpy(integers1, integers2), time_pyarrow(table)]
    df = pd.DataFrame({'Method': ['Loop', 'Numpy', 'PyArrow'], 'Time': times})

    plt.bar(df['Method'], df['Time'], color=['blue', 'orange', 'green'])

    plt.xlabel('Method')
    plt.ylabel('Computation Time (seconds)')
    plt.title('Computation Time Comparison')

    plt.savefig('computation_time_comparison.png')

def visualize_times_no_loop(integers1, integers2, table, size, run):
    plt.clf()
    times = [time_numpy(integers1, integers2), time_pyarrow(table)]
    df = pd.DataFrame({'Method': ['Numpy', 'PyArrow'], 'Time': times})

    plt.bar(df['Method'], df['Time'], color=['blue', 'orange'])

    plt.xlabel('Method')
    plt.ylabel('Computation Time (seconds)')
    plt.title('Computation Time Comparison for ' + str(size) + " indices")

    plt.savefig('computation_time_comparison_'+str(run)+'.png')

def compare(size, loop, run):
    integers1 = np.random.randint(1, 11, size=size)
    integers2 = np.random.randint(1, 11, size=size)
    names = ["integer_1", "integer_2"]
    table = pa.table([pa.array(integers1, type=pa.int16()), pa.array(integers2, type=pa.int16())], names=names)
    if(loop):
        visualize_times(integers1, integers2, table)
    else:
        visualize_times_no_loop(integers1, integers2, table, size, run)