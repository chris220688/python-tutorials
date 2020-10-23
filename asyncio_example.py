"""
	Use asyncio everywhere! But mainly if your program is network bound!

	Run the following program in a Linux machine:

		python3 asyncio.py

	While running the program, open another terminal and inspect the processes:

		ps -ef | grep asyncio.py

	You should be able to see 1 single process with 'pid' that should match with
	the 'printed' lines.
"""
import asyncio
import os


async def dummy_function(name):
	print(f'Running child process {name}, pid: {os.getpid()}')
	await asyncio.sleep(20)


async def main():
	print(f'Running parent process: {os.getpid()}')

	# Pool of tasks (threads)
	pool = []

	# Create tasks (threads)
	for name in ['A', 'B', 'C']:
		pool.append(dummy_function(name=name))

	await asyncio.gather(*pool)


if __name__ == '__main__':
	# Run tasks (threads)
	
	# Python 3
	loop = asyncio.get_event_loop()
	loop.run_until_complete(main())

	# Python 3.7+
	# asyncio.run(main())
