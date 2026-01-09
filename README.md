# MOSFET Fabrication & Process Design
This repository contains the design files, process flow documentation, and TCAD simulations for the fabrication of N-channel enhancement-mode MOSFETs. The project integrates physical process planning with automated layout generation for Maskless Lithography (MLA).
## Project Components
* Process Flow: Detailed fabrication steps documented in LaTeX.
* Layout Automation: KLayout LYM macros for generating GDSII files.
* TCAD Simulations: Predictive modeling using Silvaco ATHENA (Upcoming).
    
## Process Overview
The fabrication follows a standard self-aligned gate process. The specific parameters for oxidation, implantation, and metallization are detailed in the Process_Flow.tex file.

## Software & Automation
### KLayout Macro (LYM)
The layout is generated programmatically to ensure precision and scalability. The .lym script handles:
* Layer Definition: Active, Gate, Contact, and Metal layers.
* Parametric Design: Ability to adjust W/L ratios dynamically.
* GDS Export: Optimized for direct import into MLA systems.
To run the macro:
1) Open KLayout.
2) Go to Macros -> Macro Development.
3) Import mosfet_gen.lym and click Run.

### TCAD Simulation (Silvaco ATHENA)
Status: In Development Future updates will include .in files to simulate:
1) Dopant concentration profiles (NA​, ND​).
2) Junction depths.
3) Threshold voltage (Vth​) extraction.

## Repository Structure
```
├── docs/
│   └── Process_Flow.tex       # LaTeX source for fabrication steps
├── layout/
│   ├── mosfet_gen.lym         # KLayout Python/Ruby macro
│   └── outputs/               # Generated GDSII files
├── simulation/
│   └── athena/                # Silvaco ATHENA input scripts (Upcoming)
└── README.md
```

## Getting Started
* Documentation: Compile the LaTeX file in the docs/ folder to view the full process traveler.
* Layout: Load the script in KLayout to generate your device geometry.
* Fabrication: Use the exported GDSII file with your MLA 150 (or equivalent) lithography system.

## License
See the [LICENSE](./LICENSE) file for details.
