# Create an empty queue using a simple list
task_queue = []

# Add a new task to the queue
task_queue.append("Complete homework")
print(f"Task added: Complete homework")

# Execute the first task (FIFO)
if len(task_queue) > 0:
    executed_task = task_queue.pop(0)  # Remove and execute the first task
    print(f"Executing task: {executed_task}")
else:
    print("No tasks to execute.")

# Add another task to the queue
task_queue.append("Prepare report")
print(f"Task added: Prepare report")

# Display the pending tasks in the queue
print(f"Pending tasks: {task_queue}")

# Execute the next task
if len(task_queue) > 0:
    executed_task = task_queue.pop(0)  # Remove and execute the first task
    print(f"Executing task: {executed_task}")
else:
    print("No tasks to execute.")

# Display pending tasks after execution
print(f"Pending tasks: {task_queue}")
