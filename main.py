# EcoVision - Smart Energy Optimization Engine

def calculate_energy(power, hours):
    energy = power * hours  # Wh
    carbon = energy * 0.5   # g CO2 (example factor)
    cost = energy * 0.01    # ₹ approximate cost
    return energy, carbon, cost

def get_suggestion(energy):
    if energy > 1000:
        return "⚠ High energy usage! Reduce usage."
    else:
        return "✅ Energy usage is efficient."

def main():
    print("Welcome to EcoVision - Smart Energy Optimization\n")

    power = float(input("Enter device power in Watts: "))
    hours = float(input("Enter hours used: "))

    energy, carbon, cost = calculate_energy(power, hours)
    suggestion = get_suggestion(energy)

    print("\n--- Results ---")
    print(f"Energy Used: {energy} Wh")
    print(f"Estimated CO₂ Emission: {carbon} g")
    print(f"Estimated Cost: ₹{cost}")
    print(f"Suggestion: {suggestion}")
    print(f"If 100 homes use EcoVision: approx {carbon*100} g CO₂ saved")

if __name__ == "__main__":
    main()
    