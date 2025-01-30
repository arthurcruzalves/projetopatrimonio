from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
import sys
import csv

class LocalizarPatrimonio(QWidget):
    def __init__(self):
        super().__init__()

          
        # Vamos configurar a geometria da tela.
        # Setandos valores de posição x e y, além de largura e altura 
        self.setGeometry(10,30,400,300)

        self.setWindowTitle("Cadastro todos os equipamentos do patrimônio")

        # Gerenciador de layout vertical 
        self.layout_v = QVBoxLayout()

        # ID
        self.label_id = QLabel("ID do Objeto: ")
        self.label_id.setStyleSheet("QLabel{font-size:12pt}")

        self.edit_id = QLineEdit()
        self.edit_id.setStyleSheet("QLineEdit{font-size:12pt}")

         # números de série
        self.label_numeros = QLabel("Números de Séries: ")
        self.label_numeros.setStyleSheet("QLabel{font-size:12pt}")

        self.edit_numeros = QLineEdit()
        self.edit_numeros.setStyleSheet("QLineEdit{font-size:12pt}")

        # nome do patrimônio

        self.label_nome = QLabel("Nome do Patrimônio: ")
        self.label_nome.setStyleSheet("QLabel{font-size:12pt}")

        self.edit_nome = QLineEdit()
        self.edit_nome.setStyleSheet("QLineEdit{font-size:12pt}")

        # tipo
        self.label_tipo = QLabel("Tipo do Objeto: ")
        self.label_tipo.setStyleSheet("QLabel{font-size:12pt}")

        self.edit_tipo = QLineEdit()
        self.edit_tipo.setStyleSheet("QLineEdit{font-size:12pt}")

        # descrição
        self.label_descricao = QLabel("Descrição do Objeto: ")
        self.label_descricao.setStyleSheet("QLabel{font-size:12pt}")

        self.edit_descricao = QLineEdit()
        self.edit_descricao.setStyleSheet("QLineEdit{font-size:12pt}")

        # localização
        self.label_localizacao = QLabel("Localização do Produto: ")
        self.label_localizacao.setStyleSheet("QLabel{font-size:12pt}")

        self.edit_localizacao = QLineEdit()
        self.edit_localizacao.setStyleSheet("QLineEdit{font-size:12pt}")

        # data de fabricação
        self.label_fabricacao = QLabel("Data de Fabricação: ")
        self.label_fabricacao.setStyleSheet("QLabel{font-size:12pt}")

        self.edit_fabricacao = QLineEdit()
        self.edit_fabricacao.setStyleSheet("QLineEdit{font-size:12pt}")

        # data de aquisição
        self.label_aquisicao = QLabel("Data de Aquisição: ")
        self.label_aquisicao.setStyleSheet("QLabel{font-size:12pt}")

        self.edit_aquisicao = QLineEdit()
        self.edit_aquisicao.setStyleSheet("QLineEdit{font-size:12pt}")

    

        # Adicionar a label nome e o lineedit ao layout vertical
        self.layout_v.addWidget(self.label_id)
        self.layout_v.addWidget(self.edit_id)
        self.btnbuscar = QPushButton("Buscar Patrimônio")
        self.layout_v.addWidget(self.btnbuscar)
        self.btnbuscar.clicked.connect(self.localizar)

        self.layout_v.addWidget(self.label_numeros)
        self.layout_v.addWidget(self.edit_numeros)

        self.layout_v.addWidget(self.label_nome)
        self.layout_v.addWidget(self.edit_nome)

        self.layout_v.addWidget(self.label_tipo)
        self.layout_v.addWidget(self.edit_tipo)

        self.layout_v.addWidget(self.label_descricao)
        self.layout_v.addWidget(self.edit_descricao)

        self.layout_v.addWidget(self.label_localizacao)
        self.layout_v.addWidget(self.edit_localizacao)

        self.layout_v.addWidget(self.label_fabricacao)
        self.layout_v.addWidget(self.edit_fabricacao)

        self.layout_v.addWidget(self.label_aquisicao)
        self.layout_v.addWidget(self.edit_aquisicao)

        self.setLayout(self.layout_v)

    def localizar(self):

        # abrir o arquivo csv e atribuir a uma variável
        arquivo = open("inventario.csv","r",encoding="utf8") 
        linhas = csv.reader(arquivo)

        for i in linhas:
            lin = str(i).replace("['","").replace("']", "").split(";")
            if(lin[0]==self.edit_id.text()):
                self.edit_numeros.setText(lin[1])
                self.edit_nome.setText(lin[2])
                self.edit_tipo.setText(lin[3])
                self.edit_descricao.setText(lin[4])
                self.edit_localizacao.setText(lin[5])
                self.edit_fabricacao.setText(lin[6])
                self.edit_aquisicao.setText(lin[7])








     

#app = QApplication(sys.argv)
#tela = patrimonio()
#tela.show()
#app.exec()