import time
from matplotlib import pyplot as plt

NANO_TO_MS = 1000000.0
AVERAGES = 50

class StackRunner:
    def __init__(self):
        pass

    def RunStackList(self, runs, size, stk):
        ls_timing = 0.0

        for r in range(AVERAGES):
            start_time = time.perf_counter_ns ()
            for k in range(runs):
                for i in range ( size ) :
                    stk.push ( i )

                for j in range ( size ) :
                    stk.pop ()
            stop_time = time.perf_counter_ns ()
            ls_timing += ( (stop_time - start_time) / NANO_TO_MS )

        return  ls_timing/float(AVERAGES)

    def RunStackList2(self, runs, size, deqs, stk):
        ls_timing = 0.0

        for s in range ( size ) :
            stk.push ( size )

        for r in range(AVERAGES):
            start_time = time.perf_counter_ns()
            for k in range(runs):
                for i in range ( deqs ) :
                    stk.push ( i )

                for j in range ( deqs ) :
                    stk.pop ()

            stop_time = time.perf_counter_ns ()
            ls_timing += ( (stop_time - start_time) / NANO_TO_MS )

        return  ls_timing/float(AVERAGES)

    def plot_stack_comparisons_bg(self, stack_times_df):
        for c in stack_times_df.columns:
            plt.bar( c, stack_times_df[c] )
        plt.xticks ( rotation=45 )
        plt.ylabel('Milliseconds')
        plt.title('Stack Times')
        plt.show()