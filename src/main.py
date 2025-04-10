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
            pos = self.display.GetViewer().GetPoint(event.x(), event.y())
            self.points.append((pos[0], pos[1]))  # Store 2D point
            print(f"Clicked: {self.points[-1]}")  # Debug for now
            if len(self.points) == 2:  # Draw line between two points
                # Placeholder for line drawing—expand this later
                self.points.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CADWindow()
    window.show()
    window.start_display()
    sys.exit(app.exec_())