# ToolandDieCAD
An open-source CAD tool for tool and die makers, built with Python, PyQt5, and pythonocc-core to provide a free alternative to SolidWorks.

## Getting Started
1. Create a Conda environment: `conda create -n pyocc python=3.10 -c conda-forge`
2. Install dependencies: `conda install -c conda-forge pyqt pythonocc-core`
3. Run: `python src/main.py`
4. Current Features:
   - Displays a 3D box.
   - Records 3D points on mouse click for sketching.

## Goals
- 2D sketching with lines, circles, and constraints.
- Extrusion for die design.
- Future: assemblies, STEP/IGES export, tool-specific features.

## Development
- Built in a Conda environment (`pyocc`) with Python 3.10.
- Uses OpenCASCADE for geometry and OpenGL for rendering.
- Contributions welcome!