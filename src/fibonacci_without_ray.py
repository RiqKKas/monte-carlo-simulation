import os
import time

def fibonacci_local(sequence_size):
    fibonacci = []
    for i in range(0, sequence_size):
        if i < 2:
            fibonacci.append(i)
            continue
        fibonacci.append(fibonacci[i-1]+fibonacci[i-2])
        
    return len(fibonacci)
  
# Execução local
def run_local(sequence_size):
    # Obtem o numero de CPUs disponiveis na maquina
    cpu_count = os.cpu_count()
    
    # Total de tarefas(calculo de fibonacci) a serem executadas
    total_tasks = 24
    
    start_time = time.time()
    results = [fibonacci_local(sequence_size) for _ in range(total_tasks)]
    duration = time.time() - start_time
    
    print(('Execução Centralizada -'
          + ' Tamanho da sequência de Fibonacci: {},'
          + ' Total de Taks: {},'
          + ' Tempo de execução local: {},'
          + ' Total de CPUs: {}').format(results.pop(), total_tasks, duration, cpu_count)) 
    
run_local(100000)