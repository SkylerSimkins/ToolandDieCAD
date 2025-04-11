from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QSizePolicy
from PyQt5.QtCore import Qt
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox
from OCC.Core.Quantity import Quantity_Color, Quantity_TOC_RGB
import sys

# Load the backend before importing qtViewer3d
from OCC.Display.backend import load_backend
load_backend("pyqt5")

# Import qtViewer3d
from OCC.Display.qtDisplay import qtViewer3d

class CADWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ToolandDieCAD")
        self.setGeometry(100, 100, 800, 600)

        # Create a central widget and layout
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        self.layout.setContentsMargins(0, 0, 0, 0)  # No margins
        self.layout.setSpacing(0)  # No spacing

        # Initialize OpenCASCADE viewer within Qt
        self.display = qtViewer3d(self.central_widget)
        self.layout.addWidget(self.display)
        self.display.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  # Stretch to fill
        
        self.points = []  # Store sketch points
        
        # Start the display and configure view
        self.display.InitDriver()
        gray = Quantity_Color(0.5, 0.5, 0.5, Quantity_TOC_RGB)
        self.display._display.View.SetBgGradientColors(gray, gray, 2, True)  # Gray background
        self.display.setGeometry(0, 0, 800, 600)  # Force size after init
        self.show_shape()

    def show_shape(self):
        box = BRepPrimAPI_MakeBox(50, 50, 50).Shape()
        self.display._display.DisplayShape(box, update=True)
        self.display._display.FitAll()  # Zoom to fit the box

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            x, y = event.x(), event.y()
            try:
                x_3d, y_3d, z_3d, vx, vy, vz = self.display._display.View.ConvertWithProj(x, y)
                self.points.append((x_3d, y_3d, z_3d))
                print(f"Clicked 3D point: ({x_3d}, {y_3d}, {z_3d})")
                if len(self.points) == 2:
                    print("Ready to draw a line between points:", self.points)
                    self.points.clear()
            except Exception as e:
                print(f"Error converting coordinates: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CADWindow()
    window.show()
    sys.exit(app.exec_())