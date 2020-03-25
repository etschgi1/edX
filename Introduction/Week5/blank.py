from time import time

gen_start = time()
print(sum(n for n in range(10000000)))
gen_end = time()
gen_time = gen_end - gen_start

list_start = time()
print(sum([n for n in range(10000000)]))
list_end = time()
list_time = list_end - list_start

# generator is faster
print(f'sum(n for n in range(10000000)) took {gen_time} secs')
print(f'sum([n for n in range(10000000)]) took {list_time} secs')
