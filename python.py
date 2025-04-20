import numpy as np
import matplotlib.pyplot as plt

G = 6.67430e-11

print("Simulador de Órbita en un Campo Gravitatorio")
M = float(input("Introduce la masa del cuerpo central (kg): "))
r_mag0 = float(input("Introduce la distancia inicial del satélite (m): "))
v_mag0 = float(input("Introduce la velocidad inicial del satélite (m/s): "))
m_sat = float(input("Introduce la masa del satélite (kg): "))

dt = 10
num_steps = 10000

r0 = np.array([r_mag0, 0])
v0 = np.array([0, v_mag0])

r = np.zeros((num_steps, 2))
v = np.zeros((num_steps, 2))
r[0] = r0
v[0] = v0

for i in range(1, num_steps):
    r_mag = np.linalg.norm(r[i-1])
    acc = -G * M * r[i-1] / r_mag**3
    v[i] = v[i-1] + acc * dt
    r[i] = r[i-1] + v[i] * dt

r_final = r[-1]
v_final = v[-1]
r_final_mag = np.linalg.norm(r_final)
v_final_mag = np.linalg.norm(v_final)

energia_cinetica = 0.5 * m_sat * v_final_mag**2
energia_potencial = -G * M * m_sat / r_final_mag
energia_total = energia_cinetica + energia_potencial

print("\n--- Resultados Finales ---")
print(f"Posición final: x = {r_final[0]:.2f} m, y = {r_final[1]:.2f} m")
print(f"Velocidad final: vx = {v_final[0]:.2f} m/s, vy = {v_final[1]:.2f} m/s")
print(f"Energía cinética final: {energia_cinetica:.2e} J")
print(f"Energía potencial gravitatoria final: {energia_potencial:.2e} J")
print(f"Energía mecánica total final: {energia_total:.2e} J")

plt.figure(figsize=(8, 8))
plt.plot(r[:, 0], r[:, 1], label="Órbita del satélite")
plt.plot(0, 0, 'yo', label="Cuerpo central")
plt.xlabel("Posición X (m)")
plt.ylabel("Posición Y (m)")
plt.title("Simulación de la Órbita")
plt.legend()
plt.axis("equal")
plt.grid(True)
plt.show()
