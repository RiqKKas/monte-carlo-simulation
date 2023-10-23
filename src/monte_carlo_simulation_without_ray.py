import os
import time
import random

def monte_carlo_simulation(num_samples):
    inside_circle = 0
    for _ in range(num_samples):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:  # Correção: x^2 + y^2 em vez de x*2 + y*2
            inside_circle += 1
            
    return inside_circle

def estimate_pi(num_samples, num_clusters):
    results = [monte_carlo_simulation(num_samples // num_clusters) for _ in range(num_clusters)]
    total_inside_circle = sum(results)
    pi_estimate = (4.0 * total_inside_circle) / num_samples
    
    return pi_estimate

if __name__ == "__main__":
    num_samples = 10000000

    # Obtem o numero de CPUs disponiveis na maquina
    num_clusters = os.cpu_count()

    start_time = time.time()
    pi_estimate = estimate_pi(num_samples, num_clusters)
    end_time = time.time()

    print("=> Execução Centralizada")
    print(f"π Estimado: {pi_estimate}")
    print(f"π Real: {3.14159265358979323846}")
    print(f"Tempo Gasto: {end_time - start_time} segundos") 
    print(f"Total de CPUs: {num_clusters}")
