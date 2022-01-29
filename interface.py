import sys
from winsound import PlaySound
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton,QLabel, QLineEdit
from PyQt6 import QtGui



def ler_texto():
   valor_mensagem = caixa1.text()
   caixa1.setText(valor_mensagem)
   
   
def enviar_contato():
    valor_contato = caixa2.text()
    caixa2.setText(valor_contato)
 
   
      
    contato = caixa2.text()
    texto2.setText(contato)

app = QApplication(sys.argv)
janela = QWidget()
janela.resize(600,800)
janela.setWindowTitle('Felicia')


texto1 = QLabel("Disparos automáticos",janela)
texto1.move(150,20)
texto1.setStyleSheet('font-size:30px')

texto2 = QLabel("raul cordeiro",janela)
texto2.move(200,60)
texto2.setStyleSheet('font-size:30px')



btn_enviar_mensagem = QPushButton("enviar_mensagem",janela)
btn_enviar_mensagem.setGeometry(75,360,200,60)
btn_enviar_mensagem.setStyleSheet('background-color:green;color:white')
btn_enviar_mensagem.clicked.connect(ler_texto)

btn_enviar_contato = QPushButton("enviar_contato", janela)
btn_enviar_contato.setGeometry(75,700,200,60)
btn_enviar_contato.setStyleSheet('background-color:green;color:white')
btn_enviar_contato.clicked.connect(enviar_contato)

caixa1 = QLineEdit("", janela)
caixa1.setGeometry(50,150,250,200)

caixa2 = QLineEdit("", janela)
caixa2.setGeometry(50,490,250,200)



imagem = QLabel("",janela)
imagem.move(250, 300)
imagem.setPixmap(QtGui.QPixmap("robot.png"))

janela.show()
app.exec()

