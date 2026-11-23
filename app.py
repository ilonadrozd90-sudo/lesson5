import sys

from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QSlider,
    QSizePolicy,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)
from PySide6.QtCore import Qt, QTimer

class Window(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Start / Stop")
        self.setMinimumWidth(200)

        self.counter = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timer_method)
        self.timer.start(1000)

        self.spin_box = QSpinBox()
        self.spin_box.setRange(0, 10000)
        self.spin_box.setValue(0)
        self.spin_box.setReadOnly(True)
        self.spin_box.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)
        self.spin_box.setStyleSheet("background: lightgray;")

        self.vertical_slider = QSlider(Qt.Orientation.Vertical)
        self.vertical_slider.setRange(0, 255)
        self.secondary_spin_box = QSpinBox()
        self.secondary_spin_box.setRange(0, 255)
        self.secondary_spin_box.setReadOnly(True)
        self.secondary_spin_box.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)
        self.secondary_spin_box.setStyleSheet("background: lightgray;")

        self.color_box = QLabel()
        self.color_box.setMinimumWidth(100)
        self.color_box.setSizePolicy(
            QSizePolicy.Policy.Preferred,
            QSizePolicy.Policy.Expanding,
        )
        self.vertical_slider.valueChanged.connect(self.slider)
        self.slider(self.vertical_slider.value())

        self.toggle_button = QPushButton("Start")
        self.toggle_button.setCheckable(True)
        self.toggle_button.toggled.connect(self._update_button_text)

        value_layout = QHBoxLayout()
        value_layout.addWidget(QLabel("Value:"))
        value_layout.addWidget(self.spin_box)

        layout = QVBoxLayout()
        layout.addLayout(value_layout)
        layout.addWidget(self.toggle_button)

        slider_layout = QVBoxLayout()
        slider_layout.addWidget(self.vertical_slider)
        slider_layout.addWidget(self.secondary_spin_box)

        main_layout = QHBoxLayout()
        main_layout.addLayout(layout)
        main_layout.addLayout(slider_layout)
        main_layout.addWidget(self.color_box)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def _update_button_text(self, checked: bool) -> None:
        self.toggle_button.setText("Stop" if checked else "Start")
        if checked:
            self.counter = 0
            self.timer.start(10)
        else:
            self.timer.stop()


    def timer_method(self):
        self.counter +=1 
        self.spin_box.setValue(self.counter)

    def slider(self, value: int) -> None:
        self.secondary_spin_box.setValue(value)
        self.color_box.setStyleSheet(f"background: rgb(0, {value}, 0);")

def main() -> None:
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
