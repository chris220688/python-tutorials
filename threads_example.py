"""
	Use threads if your program is network bound!

	Run the following program in a Linux machine:

		python3 threads.py

	While running the program, open another terminal and inspect the processes:

		ps -ef | grep threads.py

	You should be able to see 1 single process with 'pid' that should match with
	the 'printed' lines.
"""
import os
import threading
import time


def dummy_function(name):
	print(f'Running child process {name}, pid: {os.getpid()}')
	time.sleep(20)


if __name__ == "__main__":
	print(f'Running parent process: {os.getpid()}')

	# Pool of threads
	pool = []

	# Create threads
	for name in ['A', 'B', 'C']:
		thread = threading.Thread(target=dummy_function, args=(name))
		pool.append(thread)
		thread.start()
	
	# Run threads
	for thread in pool:
		thread.join()
