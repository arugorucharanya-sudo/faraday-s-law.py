 Faraday's Law Calculation

 Input values
N = int(input("Enter number of turns in coil: "))
phi_initial = float(input("Enter initial magnetic flux (Wb): "))
phi_final = float(input("Enter final magnetic flux (Wb): "))
time = float(input("Enter time taken for change (s): "))

 Calculate change in flux
delta_phi = phi_final - phi_initial

 Calculate induced EMF
emf = -N * (delta_phi / time)

 Display results
print("\n--- Faraday's Law Calculation ---")
print("Number of turns =", N)
print("Initial flux =", phi_initial, "Wb")
print("Final flux =", phi_final, "Wb")
print("Change in flux =", delta_phi, "Wb")
print("Time =", time, "s")
print("Induced EMF =", emf, "V")
print("Magnitude of induced EMF =", abs(emf), "V")
