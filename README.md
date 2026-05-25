# Solar Panel Electrical Failure Simulation

A Python simulation modelling three electrical fault scenarios in a solar panel system, with supporting technical schematic produced in AutoCAD.

## Project Overview
This project simulates the power output of a solar panel system under normal conditions and three failure scenarios, using real irradiance modelling over a 24-hour period.

## Failure Scenarios Modelled
- **Partial shading** — current reduced by 40% after hour 10
- **Inverter fault** — output drops to zero when power exceeds 250W
- **Cell degradation** — voltage reduced by 20% across the full day

## Files
- `simulation.py` — main Python simulation script
- `simulation_results.csv` — exported power output data for all scenarios
- `power_output_chart.png` — graph comparing normal vs failure outputs

## Tools Used
- Python (NumPy, Matplotlib, Pandas)
- AutoCAD (system schematic with annotated failure zones)

## Inspiration
Developed as a practical follow-up to the Energy Innovation and Emerging Technologies program preview by Stanford University Online (2026).
