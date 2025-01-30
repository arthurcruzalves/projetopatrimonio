import sys 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from patrimonio import patrimonio
from localizacao import localizacao
from localizar_patrimonio import LocalizarPatrimonio

class TelaInicial(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gerenciar")
        self.setGeometry(300,200,200,150)
        self.layout_v = QVBoxLayout()

        self.label_titulo = QLabel("Clique para abrir a janela")
        self.button = QPushButton("Abrir Patrimônio")
        self.button2 = QPushButton("Abrir Localização")
        self.button3 = QPushButton("Localizar Patrimônio")

        self.layout_v.addWidget(self.label_titulo)
        self.layout_v.addWidget(self.button)
        self.layout_v.addWidget(self.button2)        
        self.layout_v.addWidget(self.button3)

        self.button.clicked.connect(self.abrir_cadastro)
        self.button2.clicked.connect(self.abrir_cadastro2)
        self.button3.clicked.connect(self.localizar_patrimonio)


        self.setLayout(self.layout_v)

    def abrir_cadastro(self):
        self.pat = patrimonio()
        self.pat.show()


    def abrir_cadastro2(self):
        self.pat = localizacao()
        self.pat.show()

    def localizar_patrimonio(self):
        self.pat = LocalizarPatrimonio()
        self.pat.show()


app = QApplication(sys.argv)
tela = TelaInicial()
tela.show()
app.exec()