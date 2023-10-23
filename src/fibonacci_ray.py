import os
import time
import ray

# Ray task
@ray.remote
def fibonacci_distributed(sequence_size):
    fibonacci = []
    for i in range(0, sequence_size):
        if i < 2:
            fibonacci.append(i)
            continue
        fibonacci.append(fibonacci[i-1]+fibonacci[i-2])
        
    return len(fibonacci)

# Execucao Remota
def run_remote(sequence_size):
    # Inicializa o ambiente Ray
    ray.init()
    
    # Obtem informações sobre os recursos disponiveis
    cluster_resources = ray.cluster_resources()
    
    # Obtem o numero de CPUs disponiveis
    cpu_count = int(cluster_resources.get("CPU", 0))
    
    # Total de tarefas(calculo de fibonacci) a serem executadas
    total_tasks = 240
    
    start_time = time.time()
    results = ray.get([fibonacci_distributed.remote(sequence_size) for _ in range(total_tasks)])
    duration = time.time() - start_time
    
    print(('Execução Distribuída -'
          + ' Tamanho da sequência de Fibonacci: {},'
          + ' Total de Taks: {},'
          + ' Tempo de execução remota: {},'
          + ' Total de CPUs: {}').format(results.pop(), total_tasks, duration, cpu_count)) 
    
run_remote(100000)