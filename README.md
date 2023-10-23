# Simulação de Monte Carlo para o Cálculo de π

<h2 id="installation">🚀&nbsp; Como executar </h2>

<b> Instale o Framework Ray em todas as máquinas disponíves para o processamento: <b>

```bash
pip install -U "ray[default]"
```

<b> Inicie o nó mestre no host principal, que será o ponto de conexão para todos os outros hosts: <b>

```bash
ray start --head
```

<b> Que retornará as seguintes informações para conexão dos nós trabalhadores: <b>

```bash

--------------------
Ray runtime started.
--------------------

Next steps
  To add another node to this Ray cluster, run
    ray start --address='ip:porta'

```

<b> Se não quiser que seu nó mestre disponibilize recursos para o processamento das tasks use: <b>

```bash
ray start --head --num-cpus 0
```

<b> A partir disso, após instalar o Framework Ray em todos os hosts que trabalharam no processamento, inicie neles a conexão com o nó mestre, a partir do comando: <b>

```bash
ray start --address="ip:porta"
```

<b> Por fim, é só executar, no nó mestre, o código com as devidas implementações do Framework Ray para ocorrer a execução distribuída: <b>

```bash
python3 monte_carlo_simulation_ray.py
```

<b> Acompanhe o status da execução distribuida a partir do comando: <b>

```bash
ray status
```

<b> Para parar o processo Ray, execute em cada máquina em execução: <b>

```bash
ray stop
```
