import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# ── 1. TIME & IRRADIANCE ──────────────────────────────────────────────────────
hours = np.arange(0, 24, 0.5)
irradiance = np.maximum(0, np.sin((hours - 6) * np.pi / 12))

# ── 2. NORMAL OPERATION ───────────────────────────────────────────────────────
voltage_normal = 36 * irradiance
current_normal = 8.5 * irradiance
power_normal   = voltage_normal * current_normal

# ── 3. FAILURE SCENARIOS ──────────────────────────────────────────────────────

# Failure 1: Partial shading (current reduced by 40% after hour 10)
current_shading = current_normal.copy()
current_shading[hours >= 10] *= 0.60
power_shading = voltage_normal * current_shading

# Failure 2: Inverter fault (output drops to zero after power exceeds 250W)
power_inverter = power_normal.copy()
power_inverter[power_inverter > 250] = 0

# Failure 3: Cell degradation (voltage drops by 20% across the whole day)
voltage_degraded = voltage_normal * 0.80
power_degraded   = voltage_degraded * current_normal

# ── 4. FAULT DETECTION FUNCTION ───────────────────────────────────────────────
def detect_fault(power, label, threshold=50):
    faults = []
    for i, p in enumerate(power):
        if p < threshold and hours[i] > 7 and hours[i] < 18:
            faults.append(hours[i])
    if faults:
        print(f"[{label}] Fault detected at hours: {faults}")
    else:
        print(f"[{label}] No faults detected.")
    return faults

print("\n── Fault Detection Results ──")
detect_fault(power_normal,   "Normal operation")
detect_fault(power_shading,  "Partial shading")
detect_fault(power_inverter, "Inverter fault")
detect_fault(power_degraded, "Cell degradation")

# ── 5. PLOT ───────────────────────────────────────────────────────────────────
plt.figure(figsize=(10, 6))
plt.plot(hours, power_normal,   label="Normal output",      linewidth=2)
plt.plot(hours, power_shading,  label="Partial shading",    linestyle="--")
plt.plot(hours, power_inverter, label="Inverter fault",     linestyle="-.")
plt.plot(hours, power_degraded, label="Cell degradation",   linestyle=":")
plt.xlabel("Hour of day")
plt.ylabel("Power (W)")
plt.title("Solar Panel Output: Normal vs Electrical Failure Scenarios")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("power_output_chart.png", dpi=150)
plt.show()
print("Chart saved as power_output_chart.png")

# ── 6. EXPORT CSV ─────────────────────────────────────────────────────────────
df = pd.DataFrame({
    "Hour":              hours,
    "Normal_W":          power_normal,
    "Shading_W":         power_shading,
    "Inverter_Fault_W":  power_inverter,
    "Degradation_W":     power_degraded
})
df.to_csv("simulation_results.csv", index=False)
print("Data saved as simulation_results.csv")