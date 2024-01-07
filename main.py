import os, time, psutil

os.system('cls')
while True:
    cpu = psutil.cpu_percent()
    cpu_deci = cpu / 100
    mem = psutil.virtual_memory().percent
    mem_deci = mem / 100

    print(f'CPU usage: {cpu:>4}%    {"█" * int(cpu_deci * 100)}{"-" * (100 - int(cpu_deci * 100))}')
    print(f'{"":~<120}')
    print(f'RAM usage: {mem:>4}%    {"█" * int(mem_deci * 100)}{"-" * (100 - int(mem_deci * 100))}')
    
    time.sleep(1)
    os.system('cls')

   