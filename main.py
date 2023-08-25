import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QListWidget, QVBoxLayout, QWidget

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window title
        self.setWindowTitle("Simple GUI Example")

        # Create a central widget and set its layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Create a button
        button = QPushButton("Click Me!")
        button.clicked.connect(self.on_button_click)
        layout.addWidget(button)

        # Create a list widget
        list_widget = QListWidget()
        layout.addWidget(list_widget)

        # Populate the list
        items = ["Item 1", "Item 2", "Item 3"]
        list_widget.addItems(items)

    def on_button_click(self):
        print("Button clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
