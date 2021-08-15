import time
from matplotlib import pyplot as plt

NANO_TO_MS = 1000000

class StackRunner:
    def __init__(self):
        pass

    def RunStackList(self, runs, size, stk):
        start_time = time.perf_counter_ns ()

        for k in range(runs):
            for i in range ( size ) :
                stk.push ( i )

            for j in range ( size ) :
                stk.pop ()

        stop_time = time.perf_counter_ns ()
        ls_timing = (stop_time - start_time) / NANO_TO_MS

        return  ls_timing

    def RunStackList2(self, runs, size, deqs, stk):
        start_time = time.perf_counter_ns ()

        for i in range ( size ) :
            stk.enqueue ( i )

        for k in range(runs):
            for i in range ( deqs ) :
                stk.enqueue ( i )

            for j in range ( deqs ) :
                stk.dequeue ()

        stop_time = time.perf_counter_ns ()
        ls_timing = (stop_time - start_time) / NANO_TO_MS

        return  ls_timing

    def plot_stack_comparisons_bg(self, stack_times_df):
        for c in stack_times_df.columns:
            plt.bar( c, stack_times_df[c] )
        plt.xticks ( rotation=45 )
        plt.ylabel('Milliseconds')
        plt.title('Stack Times')
        plt.show()