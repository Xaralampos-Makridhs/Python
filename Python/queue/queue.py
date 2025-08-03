import queue

# creates a queue with size 3
q = queue.Queue(maxsize=3)

# put()
q.put(1)
q.put(2)
q.put(3)
q.put(4)  # This will block the execution as the queue is full

# get()
print(q.get())  # prints 1, because this is the first item in the queue (FIFO)

# get_nowait()
print(q.get_nowait())  # raises queue.Empty exception because the queue is empty

# put_nowait()
print(q.put_nowait(5))  # doesn't block the program if the queue is full, raises queue.Full exception

# qsize()
print(q.qsize())  # prints the size of the queue

# empty()
print(q.empty())  # prints True if the queue is empty

# full()
print(q.full())  # prints True if the queue is full

# task_done()
q.get()  # removes the first element
q.task_done()  # marks the task as done

# join()
q.get()  # removes the first element
q.task_done()  # marks the task as done
q.join()  # waits until all tasks are done
