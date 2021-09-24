import facebook
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtWidgets

qtCreatorFile = "api.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

token= "TOKEN_APP"
page_id = 'PAGE_ID'

graph = facebook.GraphAPI(access_token = token, version = 8.0)

class VentanaPrincipal(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.pushButtonPublic.clicked.connect(self.post)
        user = graph.get_object('me', fields = 'name')
        self.LabelUser.setText(user['name'])
        
    def post(self):
        message = self.textEditMessaje.toPlainText()
        link = self.lineEditLink.text()
        self.postGraphApi(message, link)

    def postGraphApi(self, message, link):
        graph.put_object(parent_object = page_id, connection_name='feed', message=message, link=link)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec_()