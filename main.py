from PyQt6.QtWidgets import QApplication,QLabel,QWidget,QGridLayout,\
    QLineEdit,QPushButton,QComboBox
import sys
# commit: done widget class and calc method Sec45

class SpeedCalculator(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('Average Speed Calculator')
        grid=QGridLayout()

        dist_label=QLabel('Distance (km)')
        self.dist_in_box=QLineEdit()

        time_label=QLabel('Time (hours)')
        self.time_in_box=QLineEdit()

        self.std_combo_box=QComboBox()
        self.std_combo_box.addItems(['Metric (km/h)','Imperial (mph)'])

        calc_button=QPushButton('Calculate')
        calc_button.clicked.connect(self.calculate_speed)

        self.output_label=QLabel('')

        grid.addWidget(dist_label,0,0)
        grid.addWidget(self.dist_in_box,0,1)
        grid.addWidget(self.std_combo_box,0,2)
        grid.addWidget(time_label,1,0)
        grid.addWidget(self.time_in_box,1,1)
        grid.addWidget(calc_button,2,1)
        grid.addWidget(self.output_label,3,0,1,2)

        self.setLayout(grid)

    def calculate_speed(self):
        try:
            dist=float(self.dist_in_box.text())
            time=float(self.time_in_box.text())
            speed=dist/time
            if self.std_combo_box.currentIndex()==0:
                # dist metric is km
                speed=round(speed,2)
                unit='km/h'
            else:
                # dist metric is mi
                speed=round(speed*0.621371,2)
                unit='mph'
            self.output_label.setText(f'Speed is {speed} {unit}')
        except ValueError:
            self.output_label.setText('Invalid values.')

app=QApplication(sys.argv)
speed_calculator=SpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())




