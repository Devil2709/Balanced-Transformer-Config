import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from pyqtgraph import *
import matplotlib

matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import matplotlib.pyplot as plt


class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        # Drop-down menus
        self.trans_config_menu = None
        self.polarity_menu = None
        self.load_config_menu = None

        # Graph
        self.canvas = None
        self.graphWidget = None

        # Output params
        self.eff_val = None

        # Input side objects
        self.input_label = None
        self.cal_button = None

        # self.radio_StarStar = None
        # self.radio_StarDelta = None
        # self.radio_DeltaStar = None
        # self.radio_DeltaDelta = None

        # Input edit text
        self.vMag_input = None
        self.vAng_input = None
        self.impMag_input = None
        self.impAng_input = None
        self.turnsRatioNum_input = None
        self.turnsRatioDen_input = None
        self.kva_input = None
        self.ro2_input = None
        self.xo2_input = None

        # Input Labels
        self.v_label = None
        self.imp_label = None
        self.turnsRatio_label = None
        self.kva_label = None
        self.ro2_label = None
        self.xo2_label = None

        # Circuit Diagram
        self.circuit_dgm = None

        # Output Params
        self.vol_reg_out = None
        self.prim_out1 = None
        self.prim_out2 = None
        self.prim_out3 = None
        self.sec_out1 = None
        self.sec_out2 = None
        self.sec_out3 = None

        # Main window Init
        self.setWindowTitle("Test")
        geometry = self.screen().availableGeometry()
        self.setGeometry(100, 100, geometry.width() * 0.9, geometry.height() * 0.9)
        self.init_ui()
        self.showMaximized()

    def init_ui(self):

        # Drop-down Menus
        self.trans_config_menu = QComboBox()
        self.polarity_menu = QComboBox()
        self.load_config_menu = QComboBox()

        menu_ar = [self.trans_config_menu, self.polarity_menu, self.load_config_menu]
        menu_str = [['Transformer config'], [], []]

        menu_layout = QHBoxLayout()

        for i, menu in enumerate(menu_ar):

            for item in menu_str[i]:
                menu.addItem(item)

            menu.setPlaceholderText("Select Config")
            menu.setStyleSheet("QComboBox {border: 1px solid black;"
                               "border-radius: 7px;"
                               "padding: 8px;"
                               "font: 18px Ariral;"
                               "margin: 10px;}"
                               "QComboBox::drop-down {border: 0px;"
                               "margin-right: 20px;"
                               "padding: 10px;}"
                               "QComboBox::down-arrow {image: url(./icons/ic_arrow_drop_down_black_24dp.png);"
                               "height: 36px;"
                               "width: 36px;"
                               "padding: 10px;}"
                               "QComboBox QAbstractItemView {border: 1px solid black;"
                               "border-radius: 7px;"
                               "padding: 4px;"
                               "background: white;}")

            menu_layout.addWidget(menu)

        circuit_layout = QVBoxLayout()
        circuit_layout.addLayout(menu_layout)

        # Circuit Image
        self.circuit_dgm = QLabel()
        pixmp = QPixmap('img/star-delta-transfomer.jpg')
        self.circuit_dgm.setPixmap(pixmp)
        self.circuit_dgm.setStyleSheet("QLabel {border: 1px solid grey;"
                                       "border-radius: 7px;"
                                       "padding: 8px;"
                                       "background-color: white;"
                                       "margin: 10px;}")

        circuit_layout.addWidget(self.circuit_dgm, alignment=QtCore.Qt.AlignCenter)

        # Input Params
        self.vMag_input = QLineEdit()
        self.vAng_input = QLineEdit()
        self.impMag_input = QLineEdit()
        self.impAng_input = QLineEdit()
        self.turnsRatioNum_input = QLineEdit()
        self.turnsRatioDen_input = QLineEdit()
        self.kva_input = QLineEdit()
        self.ro2_input = QLineEdit()
        self.xo2_input = QLineEdit()

        self.v_label = QLabel("V Line")
        self.imp_label = QLabel("Impedance")
        self.turnsRatio_label = QLabel("Turns Ratio")
        self.kva_label = QLabel("KVA Rating")
        self.ro2_label = QLabel("Ro2")
        self.xo2_label = QLabel("Xo2")

        input_ar = [self.vMag_input, self.vAng_input, self.impMag_input, self.impAng_input, self.turnsRatioNum_input,
                    self.turnsRatioDen_input, self.kva_input, self.ro2_input, self.xo2_input]
        label_ar = [self.v_label, self.imp_label, self.turnsRatio_label, self.kva_label, self.ro2_label, self.xo2_label]
        hint_ar = ['Mag', 'Angle', 'Mag', 'Angle', 'num', 'den', 'kva', 'Ro2', 'Xo2']

        input_layout1 = QHBoxLayout()
        input_layout2 = QHBoxLayout()

        for label in label_ar:
            label.setStyleSheet("QLabel {font: 18px Ariral;}")

        for ind, input_txt in enumerate(input_ar):
            input_txt.setStyleSheet("QLineEdit {padding: 4px; border: 1px solid black;"
                                    "border-radius :7px;"
                                    "height: 40px;"
                                    "width: 90px;"
                                    "font: 18px Ariral;}")

            input_txt.setAlignment(QtCore.Qt.AlignCenter)
            input_txt.setPlaceholderText(hint_ar[ind])

        # V Line
        v_layout = QVBoxLayout()
        v_input_layout = QHBoxLayout()
        v_slash_label = QLabel('|')
        v_slash_label.setStyleSheet("QLabel {font: 20px Ariral;}")
        v_input_layout.addWidget(self.vMag_input, alignment=QtCore.Qt.AlignCenter)
        v_input_layout.addWidget(v_slash_label, alignment=QtCore.Qt.AlignCenter)
        v_input_layout.addWidget(self.vAng_input, alignment=QtCore.Qt.AlignCenter)
        v_layout.addWidget(self.v_label, alignment=QtCore.Qt.AlignCenter)
        v_layout.addLayout(v_input_layout)
        v_layout.setContentsMargins(10, 10, 10, 10)
        input_layout1.addLayout(v_layout)

        # kva rating
        kva_layout = QVBoxLayout()
        kva_layout.addWidget(self.kva_label, alignment=QtCore.Qt.AlignCenter)
        kva_layout.addWidget(self.kva_input, alignment=QtCore.Qt.AlignCenter)
        kva_layout.setContentsMargins(10, 10, 10, 10)
        input_layout1.addLayout(kva_layout)

        # Impedance
        imp_layout = QVBoxLayout()
        imp_input_layout = QHBoxLayout()
        imp_slash_label = QLabel('|')
        imp_slash_label.setStyleSheet("QLabel {font: 20px Ariral;}")
        imp_input_layout.addWidget(self.impMag_input, alignment=QtCore.Qt.AlignCenter)
        imp_input_layout.addWidget(imp_slash_label, alignment=QtCore.Qt.AlignCenter)
        imp_input_layout.addWidget(self.impAng_input, alignment=QtCore.Qt.AlignCenter)
        imp_layout.addWidget(self.imp_label, alignment=QtCore.Qt.AlignCenter)
        imp_layout.addLayout(imp_input_layout)
        imp_layout.setContentsMargins(10, 10, 10, 10)
        input_layout1.addLayout(imp_layout)

        # Ro2 rating
        ro2_layout = QVBoxLayout()
        ro2_layout.addWidget(self.ro2_label, alignment=QtCore.Qt.AlignCenter)
        ro2_layout.addWidget(self.ro2_input, alignment=QtCore.Qt.AlignCenter)
        ro2_layout.setContentsMargins(10, 10, 10, 10)
        input_layout2.addLayout(ro2_layout)

        # Turns Ratio
        turns_ratio_layout = QVBoxLayout()
        turns_ratio_input_layout = QHBoxLayout()
        turns_ratio_slash_label = QLabel('/')
        turns_ratio_slash_label.setStyleSheet("QLabel {font: 20px Ariral;}")
        turns_ratio_input_layout.addWidget(self.turnsRatioNum_input, alignment=QtCore.Qt.AlignCenter)
        turns_ratio_input_layout.addWidget(turns_ratio_slash_label, alignment=QtCore.Qt.AlignCenter)
        turns_ratio_input_layout.addWidget(self.turnsRatioDen_input, alignment=QtCore.Qt.AlignCenter)
        turns_ratio_layout.addWidget(self.turnsRatio_label, alignment=QtCore.Qt.AlignCenter)
        turns_ratio_layout.addLayout(turns_ratio_input_layout)
        turns_ratio_layout.setContentsMargins(10, 10, 10, 10)
        input_layout2.addLayout(turns_ratio_layout)

        # xo2 rating
        xo2_layout = QVBoxLayout()
        xo2_layout.addWidget(self.xo2_label, alignment=QtCore.Qt.AlignCenter)
        xo2_layout.addWidget(self.xo2_input, alignment=QtCore.Qt.AlignCenter)
        xo2_layout.setContentsMargins(10, 10, 10, 10)
        input_layout2.addLayout(xo2_layout)

        # Calculate Button
        self.cal_button = QPushButton("Calculate", self)
        self.cal_button.setStyleSheet("QPushButton {border: 1px solid grey;"
                                      "border-radius: 7px;"
                                      "background-color: white;"
                                      "height: 60px;"
                                      "width: 150px;"
                                      "font: 18px Ariral;"
                                      "margin: 10px;}"
                                      "QPushButton::pressed {border: 2px solid grey;}")
        self.cal_button.animateClick()

        bottom_layout = QVBoxLayout()
        bottom_layout.addLayout(input_layout1)
        bottom_layout.addLayout(input_layout2)
        bottom_layout.addWidget(self.cal_button, alignment=QtCore.Qt.AlignCenter)

        input_grp = QGroupBox()
        input_grp.setLayout(bottom_layout)
        input_grp.setStyleSheet("QGroupBox {font: 20px Ariral;"
                                "background-color: #EEEEEE;"
                                "border: 1px solid grey;"
                                "border-radius: 7px;"
                                "margin: 4px;"
                                "padding: 8px;}")

        circuit_grp = QGroupBox()
        circuit_grp.setLayout(circuit_layout)
        circuit_grp.setStyleSheet("QGroupBox {font: 20px Ariral;"
                                  "background-color: #EEEEEE;"
                                  "border: 1px solid grey;"
                                  "border-radius: 7px;"
                                  "margin: 4px;"
                                  "padding-bottom: 8px;}")

        left_layout = QVBoxLayout()
        left_layout.addWidget(circuit_grp)
        left_layout.addWidget(input_grp)

        # Graph
        graph_layout = QHBoxLayout()
        self.graphWidget = plt.figure()
        self.canvas = FigureCanvasQTAgg(self.graphWidget)
        ax = self.graphWidget.add_subplot(111, projection='polar')
        # ax.set_rticks([])
        ax.plot([0, 45], [0, 35], 'ro-')
        graph_layout.addWidget(self.canvas)

        graph_grp = QGroupBox()
        graph_grp.setLayout(graph_layout)
        graph_grp.setStyleSheet("QGroupBox {font: 20px Ariral;"
                                "background-color: white;"
                                "border: 1px solid grey;"
                                "border-radius: 7px;"
                                "margin: 4px;"
                                "padding-bottom: 8px;}")

        # Output
        self.vol_reg_out = QLabel("Nil")
        self.prim_out1 = QLabel("Nil")
        self.prim_out2 = QLabel("Nil")
        self.prim_out3 = QLabel("Nil")
        self.sec_out1 = QLabel("Nil")
        self.sec_out2 = QLabel("Nil")
        self.sec_out3 = QLabel("Nil")

        # Headings
        vol_reg_head = QLabel("Voltage Regulation")
        out_prim_head = QLabel("Primary Currents")
        out_sec_head = QLabel("Secondary Currents")

        out_prim_head.setStyleSheet("QLabel {font: 20px Ariral;"
                                    "margin: 5px;}")
        out_sec_head.setStyleSheet("QLabel {font: 20px Ariral;"
                                   "margin: 5px;}")
        vol_reg_head.setStyleSheet("QLabel {font: 20px Ariral;"
                                   "margin-bottom: 5px;"
                                   "margin-top: 11px}")

        out_prim_head.setAlignment(QtCore.Qt.AlignCenter)
        out_sec_head.setAlignment(QtCore.Qt.AlignCenter)
        vol_reg_head.setAlignment(QtCore.Qt.AlignCenter)

        out_text_ar = [self.vol_reg_out, self.prim_out1, self.prim_out2, self.prim_out3, self.sec_out1, self.sec_out2,
                       self.sec_out3]
        for out_text in out_text_ar:
            out_text.setStyleSheet("QLabel {border: 1px solid grey;"
                                   "border-radius: 7px;"
                                   "font: 18px Ariral;"
                                   "background-color: #FFFFFF;"
                                   "padding: 8px;"
                                   "margin: 10px;}")

            out_text.setFixedSize(150, 65)
            out_text.setAlignment(QtCore.Qt.AlignCenter)

        out_prim_layout = QHBoxLayout()
        out_sec_layout = QHBoxLayout()

        for i in range(1, 4):
            out_prim_layout.addWidget(out_text_ar[i], alignment=QtCore.Qt.AlignCenter)

        for i in range(4, 7):
            out_sec_layout.addWidget(out_text_ar[i], alignment=QtCore.Qt.AlignCenter)

        output_layout = QVBoxLayout()
        output_layout.addWidget(vol_reg_head)
        output_layout.addWidget(self.vol_reg_out, alignment=QtCore.Qt.AlignCenter)
        output_layout.addWidget(out_prim_head, alignment=QtCore.Qt.AlignCenter)
        output_layout.addLayout(out_prim_layout)
        output_layout.addWidget(out_sec_head, alignment=QtCore.Qt.AlignCenter)
        output_layout.addLayout(out_sec_layout)

        output_grp = QGroupBox()
        output_grp.setLayout(output_layout)
        output_grp.setStyleSheet("QGroupBox {font: 20px Ariral;"
                                 "background-color: #EEEEEE;"
                                 "border: 1px solid grey;"
                                 "border-radius: 7px;"
                                 "margin: 4px;"
                                 "padding-bottom: 8px;}")

        right_layout = QVBoxLayout()
        right_layout.addWidget(graph_grp)
        right_layout.addWidget(output_grp)

        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)
        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication()
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
