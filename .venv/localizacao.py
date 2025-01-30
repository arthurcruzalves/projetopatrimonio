from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
import sys

class localizacao(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(15,30,400,200)
        self.setWindowTitle("Cadastrar as localizações dos patrimônios")
        self.layout_v = QVBoxLayout()

        # ID
        self.label_id = QLabel("ID de localização: ")
        self.label_id.setStyleSheet("QLabel{font-size:12pt}")

        self.edit_id = QLineEdit()
        self.edit_id.setStyleSheet("QLineEdit{font-size:pt}")

        # empresa
        self.label_empresa = QLabel("Localização da Empresa: ")
        self.label_empresa.setStyleSheet("QLabel{font-size:12pt}")

        self.edit_empresa = QLineEdit()
        self.edit_empresa.setStyleSheet("QLineEdit{font-size:12pt}")

        # logradouro
        self.label_logradouro = QLabel("Logradouro: ")
        self.label_logradouro.setStyleSheet("QLabel{font-size:12pt}")

        self.edit_logradouro = QLineEdit()
        self.edit_logradouro.setStyleSheet("QLineEdit{font-size:12pt}")

        # nuúmero
        self.label_numero = QLabel("Número: ")
        self.label_numero.setStyleSheet("QLabel{font-size:12pt}")

        self.edit_numero = QLineEdit()
        self.edit_numero.setStyleSheet("QLineEdit{font-size:12pt}")

        # prédio
        self.label_predio = QLabel("Prédio: ")
        self.label_predio.setStyleSheet("QLabel{font-size:12pt}")

        self.edit_predio = QLineEdit()
        self.edit_predio.setStyleSheet("QLineEdit{font-size:12pt}")

        # andar
        self.label_andar = QLabel("Andar: ")
        self.label_andar.setStyleSheet("QLabel{font-size:12pt}")

        self.edit_andar = QLineEdit()
        self.edit_andar.setStyleSheet("QLineEdit{font-size:12pt}")

        # sala
        self.label_sala = QLabel("Sala: ")
        self.label_sala.setStyleSheet("QLabel{font-size:12pt}")

        self.edit_sala = QLineEdit()
        self.edit_sala.setStyleSheet("QLineEdit{font-size:12pt}")


        self.button = QPushButton("Cadastrar")
        self.button.setStyleSheet("QPushButton{background-color:blue;color:white;font-size:12pt;font-weight:bold}")

        self.button.clicked.connect(self.cadastrar)


        # Adicionar a label nome e o lineedit ao layout vertical
        self.layout_v.addWidget(self.label_id)
        self.layout_v.addWidget(self.edit_id)

        self.layout_v.addWidget(self.label_empresa)
        self.layout_v.addWidget(self.edit_empresa)

        self.layout_v.addWidget(self.label_logradouro)
        self.layout_v.addWidget(self.edit_logradouro)

        self.layout_v.addWidget(self.label_numero)
        self.layout_v.addWidget(self.edit_numero)

        self.layout_v.addWidget(self.label_predio)
        self.layout_v.addWidget(self.edit_predio)

        self.layout_v.addWidget(self.label_andar)
        self.layout_v.addWidget(self.edit_andar)

        self.layout_v.addWidget(self.label_sala)
        self.layout_v.addWidget(self.edit_sala)

        self.layout_v.addWidget(self.button)

        # Adicionar o layout_v a tela 
        self.setLayout(self.layout_v)

    
    def cadastrar(self):
        arquivo = open("patrimônio.txt","+a")
        arquivo.write(f"ID do Objeto: {self.edit_id.text()}\n")
        arquivo.write(f"Números de Séries: {self.edit_empresa.text()}\n")
        arquivo.write(f"Nome do Patrimônio: {self.edit_logradouro.text()}\n")
        arquivo.write(f"Tipo do Objeto: {self.edit_numero.text()}\n")
        arquivo.write(f"Descrição do Objeto: {self.edit_predio.text()}\n")
        arquivo.write(f"Localização do Produto: {self.edit_andar.text()}\n")
        arquivo.write(f"Data de Fabricação: {self.edit_sala.text()}\n")
        arquivo.write("--------------------------------------------------------------\n")
        arquivo.close



#app = QApplication(sys.argv)
#tela = localizacao()
#tela.show()
#app.exec()