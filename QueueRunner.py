import time
from matplotlib import pyplot as plt

NANO_TO_MS = 1000000.0
AVERAGES = 10

class QueueRunner:
    def __init__(self):
        pass

    def RunQueueList(self, runs, size, qu):
        ls_timing = 0.0

        for r in range(AVERAGES):
            start_time = time.perf_counter_ns()
            for k in range(runs):
                for i in range ( size ) :
                    qu.enqueue ( i )

                for j in range ( size ) :
                    qu.dequeue ()

            stop_time = time.perf_counter_ns ()
            ls_timing += ( (stop_time - start_time) / NANO_TO_MS )
        return  ls_timing / float(AVERAGES)

    def RunQueueList2(self, runs, size, deqs, qu):
        ls_timing = 0.0

        for i in range(size):
            qu.enqueue(i)

        for r in range(AVERAGES):
            start_time = time.perf_counter_ns ()
            for k in range(runs):
                for i in range ( deqs ) :
                    qu.enqueue ( i )

                for j in range ( deqs ) :
                    qu.dequeue ()

            stop_time = time.perf_counter_ns ()
            ls_timing += ( (stop_time - start_time) / NANO_TO_MS )
        return  ls_timing / float(AVERAGES)

    def plot_queue_comparisons_bg(self, queue_times_df):
        for c in queue_times_df.columns:
            plt.bar( c, queue_times_df[c] )
        plt.xticks ( rotation=45 )
        plt.ylabel('Milliseconds')
        plt.title('Queue Times')
        plt.show()