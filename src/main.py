from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import Qt
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox
from OCC.Display.SimpleGui import init_display
import sys

class CADWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ToolandDieCAD")
        self.setGeometry(100, 100, 800, 600)
        self.display, self.start_display, self.add_menu, self.add_function_to_menu = init_display()
        self.points = []  # Store sketch points
        self.show_shape()

    def show_shape(self):
        box = BRepPrimAPI_MakeBox(50, 50, 50).Shape()
        self.display.DisplayShape(box, update=True)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            x, y = event.x(), event.y()
            try:
                # Use V3d_View to convert 2D mouse coordinates to 3D
                x_3d, y_3d, z_3d, vx, vy, vz = self.display.view.ConvertWithProj(x, y)
                self.points.append((x_3d, y_3d, z_3d))
                print(f"Clicked 3D point: {self.points[-1]}")
                if len(self.points) == 2:
                    print("Ready to draw a line between points:", self.points)
                    self.points.clear()  # Reset for next sketch
            except Exception as e:
                print(f"Error converting coordinates: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CADWindow()
    window.show()
    window.start_display()
    sys.exit(app.exec_())