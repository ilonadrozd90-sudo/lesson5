import sys

from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)


class Window(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Start / Stop")

        self.spin_box = QSpinBox()
        self.spin_box.setRange(10, 10000)
        self.spin_box.setValue(10)

        self.toggle_button = QPushButton("Start")
        self.toggle_button.setCheckable(True)
        self.toggle_button.toggled.connect(self._update_button_text)

        value_layout = QHBoxLayout()
        value_layout.addWidget(QLabel("Value:"))
        value_layout.addWidget(self.spin_box)

        layout = QVBoxLayout()
        layout.addLayout(value_layout)
        layout.addWidget(self.toggle_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def _update_button_text(self, running: bool) -> None:
        self.toggle_button.setText("Stop" if running else "Start")


def main() -> None:
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
