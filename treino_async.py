import asyncio
import time.perf_counter

async def acordar():
	start = perf_counter()
	print("Acordando")
	await asyncio.sleep(3)
	print("Terminei de acordar")
	end = perf_counter()
	return 


async def trabalhar():
	start = perf_counter()
	print("Trabalhando")
	await asyncio.sleep(3)
	print("Terminei o expediente")
	end = perf_counter()
	return await asyncio.sleep(3)

async def almoco():
	start = perf_counter()
	print("Fazendo almoço")
	await asyncio.sleep(3)
	print("Terminei de fazer o almoço")
	end = perf_counter()
	return 

async def lavar_roupa():
	start = perf_counter()
	print("Lavando roupa")
	await asyncio.sleep(3)
	print("Terminei de lavar roupa")
	end = perf_counter()
	return 

async def main():
	start = perf_counter()

	fila = [asyncio.create_task()]


	end = perf_counter()

	delta = end - star
	return asyncio.run(queue) | None


if __name__=='__main__':
	asyncio.run(main())

