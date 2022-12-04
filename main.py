import sys
import joblib
from sklearn.ensemble import RandomForestRegressor
from PyQt5 import QtWidgets
import mainf

class Predictor():
    def __init__(self):
        self.model = joblib.load("vpr_random_forest.joblib")

    def predict(self, IW, IF, VW, FP):
        x = [[IW, IF, VW, FP]]
        res = self.model.predict(x)
        return res

class VPRApp(QtWidgets.QMainWindow, mainf.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.predictor = Predictor()
        self.setupUi(self)  # инициализация
        self.ExitButton.clicked.connect(self.ExitApp)
        self.PredictButton.clicked.connect(self.Predict)

    def ExitApp(self):
        exit(0)

    def Predict(self):
        iw = self.spinBoxIW.value() + 0.0
        ifv = self.spinBoxIF.value() + 0.0
        vw = self.doubleSpinBoxVW.value()
        fp = self.spinBoxFP.value() + 0.0

        pv = self.predictor.predict(iw, ifv, vw, fp)
        self.labelPredictHeigth.setText(f"{pv[0][0]:.2f}")
        self.labelPredictWidth.setText(f"{pv[0][1]:.2f}")

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = VPRApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()