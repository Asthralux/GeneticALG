import random

# Tamaño del Cromosoma
chromosome_size = 20

# Tamaño de la población
population_size = 100

# Tasa de cruce (Crossover Rate)
crossover_rate = 0.6

# Tasa de mutación (Mutation Rate)
mutation_rate = 0.5


# Función para inicializar la población con cromosomas aleatorios
def initialize_population(population_size, chromosome_size):
    # Genera una lista de listas, donde cada sublista representa un cromosoma y es una lista de genes (1 o 0) aleatorios.
    return [[random.randint(0, 1) for _ in range(chromosome_size)] for _ in range(population_size)]


# Función de fitness que cuenta el número de 1's en el cromosoma
def fitness(chromosome):
    # Suma los valores en el cromosoma (suma de 1's).
    return sum(chromosome)


# Función para seleccionar los padres usando el método de Roulette Wheel
def selection(population):
    # Calcula el fitness total de la población
    total_fitness = sum(fitness(chromosome) for chromosome in population)
    # Selecciona un valor aleatorio entre 0 y el fitness total
    pick = random.uniform(0, total_fitness)
    current = 0
    # Recorre la población y regresa el primer cromosoma que hace que la suma sea mayor que el valor seleccionado
    for chromosome in population:
        current += fitness(chromosome)
        if current > pick:
            print(f"De la ruleta se seleccionó el siguiente cromosoma: {chromosome}")
            return chromosome


# Función para hacer el crossover/reproducción
def crossover(parent1, parent2):
    # Selecciona un punto de cruce aleatorio
    if random.random() < crossover_rate:
        # Crea los hijos intercambiando las partes del cromosoma después del punto de cruce
        crossover_point = random.randint(0, chromosome_size - 1)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        print(f"Punto de cruce: {crossover_point}, padres: {parent1}, {parent2}, hijos: {child1}, {child2}")
        return child1, child2
    else:
        # Si no ocurre crossover, los hijos son una copia exacta de los padres
        print(f"No hubo cruce, padres: {parent1}, {parent2}")
        return parent1, parent2


# Función para mutar un cromosoma
def mutate(chromosome):
    # Cambia aleatoriamente el valor de los genes basado en la tasa de mutación
    mutated_chromosome = [gene if random.random() > mutation_rate else abs(gene - 1) for gene in chromosome]
    print(f"Cromosoma antes de mutar: {chromosome}, después de mutar: {mutated_chromosome}")
    return mutated_chromosome


# Inicializa la población
population = initialize_population(population_size, chromosome_size)
print(f"Población inicial: {population}")

# Contador de iteraciones
iteration = 0

# Ciclo principal del algoritmo genético
while True:
    iteration += 1
    print(f"Iteración número: {iteration}")
    new_population = []
    for _ in range(population_size // 2):
        # Selecciona los padres
        parent1 = selection(population)
        parent2 = selection(population)
        # Realiza el crossover y la mutación
        child1, child2 = crossover(parent1, parent2)
        new_population.extend([mutate(child1), mutate(child2)])
        # Reemplaza la población antigua con la nueva
    population = new_population
    print(f"Nueva población: {population}")

    # Verifica si alguna de las soluciones tiene fitness máximo
    for chromosome in population:
        if fitness(chromosome) == chromosome_size:
            print(f"Encontramos una solución en la iteración número {iteration}: {chromosome}")
            exit(0)
