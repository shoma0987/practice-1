import time

t1 = time.time()

a = [1,2,3]
print(a[2])

t2 = time.time()

elapsed_time = t2 - t1
print(f"経過時間:{elapsed_time}")