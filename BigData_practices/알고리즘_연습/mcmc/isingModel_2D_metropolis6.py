import numpy as np
import matplotlib.pyplot as plt
import random
from multiprocessing import Pool

class IsingModel2D:
    def __init__(self, size, temperature, external_field, exchange_interaction):
        self.size = size
        self.temperature = temperature
        self.external_field = external_field
        self.exchange_interaction = exchange_interaction
        self.spins = np.random.choice([-1, 1], size=(size, size))

    def calculate_energy_change(self, i, j):
        top = self.spins[(i-1)%self.size, j]
        bottom = self.spins[(i+1)%self.size, j]
        left = self.spins[i, (j-1)%self.size]
        right = self.spins[i, (j+1)%self.size]
        neighbor_sum = top + bottom + left + right
        delta_energy = 2 * self.spins[i, j] * (self.exchange_interaction * neighbor_sum + self.external_field)
        return delta_energy

    def metropolis_step(self):
        for _ in range(self.size**2):
            i, j = random.randint(0, self.size-1), random.randint(0, self.size-1)
            delta_energy = self.calculate_energy_change(i, j)
            if delta_energy < 0 or random.random() < np.exp(-delta_energy / self.temperature):
                self.spins[i, j] *= -1

    def simulate(self, steps, equilibration_steps):
        magnetizations = []
        for step in range(steps + equilibration_steps):
            self.metropolis_step()
            if step >= equilibration_steps:
                magnetization = np.mean(self.spins)
                magnetizations.append(magnetization)
        return np.mean(magnetizations)

def simulate_temperature(args):
    size, temperature, steps, equilibration_steps = args
    model = IsingModel2D(size, temperature, 0.01, 1)
    return model.simulate(steps, equilibration_steps)

def plot_magnetization_vs_temperature(sizes, steps, equilibration_steps, temperatures):
    plt.figure(figsize=(10, 8))

    for size in sizes:
        with Pool(processes=4) as pool:
            results = pool.map(simulate_temperature, [(size, temp, steps, equilibration_steps) for temp in temperatures])
        
        plt.plot(temperatures, results, 'o', linestyle='none', label=f'Size = {size}')

    plt.xlabel('Temperature')
    plt.ylabel('Average Magnetization')
    plt.title('Average Magnetization vs. Temperature for Different Lattice Sizes')
    plt.grid(True)
    plt.legend()
    plt.show()

# Simulation parameters
sizes = [20, 40, 60]
temperatures = np.linspace(0.1, 3.0, 50)
steps = 1000
equilibration_steps = 100

plot_magnetization_vs_temperature(sizes, steps, equilibration_steps, temperatures)