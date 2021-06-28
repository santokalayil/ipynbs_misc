import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5 import QtWidgets

def window():
	app = QApplication(sys.argv)
	w = QWidget()
	b = QLabel(w)
	b.setText("Congratulations !")
	w.setGeometry(100,100,200,50)
	b.move(50,20)
	w.setWindowTitle('Santa App')
	w.show()
	sys.exit(app.exec_())
	
if __name__ == '__main__':
	print(dir(QtWidgets))
	window()
