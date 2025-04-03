"""
Name:           producer-consumer-bounded-buffer.py
Author:         Martin F. O'Connor (C)
Description:    Implements the Producer Consumer pattern using a bounded buffer.
How to run:		To run this program from the Console/Terminal, type:
					python producer-consumer-bounded-buffer.py
Date:           28th March 2023
Version:        1.3
"""

from queue import Queue
import random
import threading
import time

BUFFER_SIZE = 8     # max buffer size
NUM_OF_ITEMS = 40   # total number of items to process
SENTINEL = "END"    # Indicate no more items to produce.


class Producer:
    """The Producer class which produces a number of items and places them into a queue."""

    def __init__(self, queue, number_of_items=NUM_OF_ITEMS):
        self.queue = queue
        self.number_of_items = number_of_items
        self.start_value  = 1        # first value (one) to be placed in queue

    def run(self):
        for _ in range(self.number_of_items):

            # if the queue is full, wait a moment (between 0 and 1 seconds).
            while self.queue.full():
                time.sleep(random.random())

            # Place an item in the queue
            self.queue.put(self.start_value)

            # Let the user know an item has been placed in the queue
            print("Producer: placed item  {0} in queue. Queue size now {1}".format(self.start_value, self.queue.qsize()))

            # Increment the start value to simulate creating a new item
            self.start_value  += 1

            # Wait a moment (between 0 and 1 seconds).
            time.sleep(random.random())

        # The producer has finished producing items.
        # Thus, place the sentinel in the queue which will indicate to the consumer thread
        # that the producer has finished producing items.
        self.queue.put(SENTINEL)
        print("Producer: placed sentinel in queue. The producer will be closed."
                + " Queue size now {0}. ".format(self.queue.qsize()))


class Consumer:
    """The Consumer class consumes items from queue until sentinel is received."""
    def __init__(self, queue):
        self.queue = queue

    def run(self):
        while True:
            if not self.queue.empty():
                item = self.queue.get()
                if item != SENTINEL:
                    self.queue.task_done()
                    print("Consumer: removed item {0} from queue. Queue size now {1}".format(item, self.queue.qsize()))
                else:
                    print("Consumer: received sentinel. The consumer will be closed.")
                    self.queue.task_done()
                    break
            time.sleep(random.random())


def main():
    # Create a Queue (buffer)
    q = Queue(maxsize=BUFFER_SIZE)

    # Create a producer object and thread.
    producer = Producer(q)
    producer_thread = threading.Thread(target=producer.run)

    # Create a consumer object and thread.
    consumer = Consumer(q)
    consumer_thread = threading.Thread(target=consumer.run)

    # Start producing items and placing them in the queue.
    producer_thread.start()

    # Delay two seconds to give the producer time to make a few items.
    time.sleep(2)

    # Start consuming items from the queue.
    consumer_thread.start()

    # Pause the program until both threads (producer and consumer) have finished.
    q.join()


if __name__ == "__main__":
    main()