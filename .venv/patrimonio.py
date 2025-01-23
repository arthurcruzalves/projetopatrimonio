from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
import sys

class patrimonio(QWidget):
    def __init__(self):
        super().__init__()

          
        # Vamos configurar a geometria da tela.
        # Setandos valores de posição x e y, além de largura e altura 
        self.setGeometry(10,30,400,300)

        self.setWindowTitle("Cadastro do patrimônio")

        # Gerenciador de layout vertical 
        self.layout_v = QVBoxLayout()

        # ID
        self.label_id = QLabel("ID do Objeto: ")
        self.label_id.setStyleSheet("QLabel{font-size:12pt}")

        self.edit_id = QLineEdit()
        self.edit_id.setStyleSheet("QLineEdit{font-size:14pt}")

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

        self.button = QPushButton("Cadastrar")
        self.button.setStyleSheet("QPushButton{background-color:blue;color:white;font-size:12pt;font-weight:bold}")

        # chamar a função de cadastro do 
        # cliente ao clicar no botão
        self.button.clicked.connect(self.cadastrar)

        # Adicionar a label nome e o lineedit ao layout vertical
        self.layout_v.addWidget(self.label_id)
        self.layout_v.addWidget(self.edit_id)

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

        self.layout_v.addWidget(self.button)


        # Adicionar o layout_v a tela 
        self.setLayout(self.layout_v)


    def cadastrar(self):
        arquivo = open("patrimônio.txt","+a")
        arquivo.write(f"ID do Objeto: {self.edit_id.text()}\n")
        arquivo.write(f"Números de Séries: {self.edit_numeros.text()}\n")
        arquivo.write(f"Nome do Patrimônio: {self.edit_nome.text()}\n")
        arquivo.write(f"Tipo do Objeto: {self.edit_tipo.text()}\n")
        arquivo.write(f"Descrição do Objeto: {self.edit_descricao.text()}\n")
        arquivo.write(f"Localização do Produto: {self.edit_localizacao.text()}\n")
        arquivo.write(f"Data de Fabricação: {self.edit_fabricacao.text()}\n")
        arquivo.write(f"Data de Aquisição: {self.edit_aquisicao.text()}\n")
        arquivo.write("--------------------------------------------------------------\n")
        arquivo.close

app = QApplication(sys.argv)
tela = patrimonio()
tela.show()
app.exec()