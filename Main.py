from QueueRunner import QueueRunner
from Queues import QueueLinkedList
from Queues import QueueList
import pandas as pd

sr = QueueRunner ()

queue_times_df = pd.DataFrame ()

queue_times_df["100-1000_L"] = [sr.RunQueueList(100, 1000, QueueList())]
queue_times_df["100-1000_LL"] = [sr.RunQueueList ( 100, 1000, QueueLinkedList () )]

queue_times_df["1-100000_L"] = [sr.RunQueueList(1, 100000, QueueList())]
queue_times_df["1-100000_LL"] = [sr.RunQueueList ( 1, 100000, QueueLinkedList () )]

queue_times_df["100000-1_L"] = [sr.RunQueueList(100000, 1, QueueList())]
queue_times_df["100000-1_LL"] = [sr.RunQueueList ( 100000, 1, QueueLinkedList () )]
