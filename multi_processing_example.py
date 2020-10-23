"""
	Use multi processing if your program is CPU bound!

	Run the following program in a Linux machine:

		python3 multi_processing.py

	While running the program, open another terminal and inspect the processes:

		ps -ef | grep multi_processing

	You should be able to see 4 different processes (1 parent and 3 children)
	with 'pid' that should match with the 'printed' lines.
"""
import multiprocessing
import os
import time


def dummy_function(name):
	print(f'Running child process {name}, pid: {os.getpid()}')
	time.sleep(20)


if __name__ == '__main__':
	print(f'Running parent process: {os.getpid()}')

	# Pool of processes
	pool = []

	# Create processes
	for name in ['A', 'B', 'C']:
		process = multiprocessing.Process(target=dummy_function, args=(name))
		pool.append(process)
		process.start()
	
	# Run processes
	for process in pool:
		process.join()
