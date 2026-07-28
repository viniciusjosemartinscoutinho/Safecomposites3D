# & "C:/Program Files/Python311/python.exe" C:\Users\ucfil\Desktop\desktop\codes\all\FEA\V\Language.py
from pathlib import Path
import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QPainter, QFont, QColor, QIcon
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QGridLayout,
    QVBoxLayout, QGraphicsDropShadowEffect,
)
import sys, os

if getattr(sys, "frozen", False):
    if sys.stdout is None or sys.stderr is None:
        devnull = open(os.devnull, "w")
        if sys.stdout is None: sys.stdout = devnull
        if sys.stderr is None: sys.stderr = devnull
    base = sys._MEIPASS
    os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = os.path.join(base, "PySide6", "plugins", "platforms")

SCRIPT_DIR = Path(__file__).resolve().parent
LOGO_PATH = SCRIPT_DIR / "Safecomposites3D-logo.jpg"

# idiomas suportados: nome (usado no keys.txt) -> texto do botao
IDIOMAS = {
    "english": "English",
    "français": "Français",
}


class JanelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.langue = None

        self.setWindowTitle("Safecomposites3D — EN/FR")
        self.setMinimumSize(920, 660)
        self.resize(1000, 700)

        self._fundo = None
        if LOGO_PATH.exists():
            self.setWindowIcon(QIcon(str(LOGO_PATH)))
            pix = QPixmap(str(LOGO_PATH))
            if not pix.isNull():
                self._fundo = pix

        self._montar_ui()

    # ---------- fundo com a imagem ----------
    def paintEvent(self, event):
        painter = QPainter(self)
        if self._fundo is not None:
            escalado = self._fundo.scaled(
                self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation
            )
            x = (self.width() - escalado.width()) // 2
            y = (self.height() - escalado.height()) // 2
            painter.drawPixmap(x, y, escalado)
        else:
            painter.fillRect(self.rect(), QColor("#0d0d12"))

        # overlay escuro por cima da imagem, pra dar legibilidade ao texto
        painter.fillRect(self.rect(), QColor(8, 8, 16, 190))
        painter.end()
        super().paintEvent(event)

    # ---------- montagem da interface ----------
    def _montar_ui(self):
        layout_geral = QVBoxLayout(self)
        layout_geral.setContentsMargins(60, 46, 60, 40)
        layout_geral.setSpacing(26)

        titulo = QLabel("Safecomposites3D")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setFont(QFont("Segoe UI", 22, QFont.Bold))
        titulo.setStyleSheet("color: rgba(220, 200, 255, 235); letter-spacing: 4px;")
        layout_geral.addWidget(titulo)

        label_pergunta = QLabel("What's the language? / Quelle est la langue ?")
        label_pergunta.setAlignment(Qt.AlignCenter)
        label_pergunta.setWordWrap(True)
        label_pergunta.setFont(QFont("Segoe UI", 26, QFont.Bold))
        label_pergunta.setStyleSheet("color: #ffffff;")

        sombra = QGraphicsDropShadowEffect()
        sombra.setBlurRadius(30)
        sombra.setOffset(0, 3)
        sombra.setColor(QColor(0, 0, 0, 230))
        label_pergunta.setGraphicsEffect(sombra)

        layout_geral.addWidget(label_pergunta)

        grade = QGridLayout()
        grade.setSpacing(14)

        for i, (nome, texto_botao) in enumerate(IDIOMAS.items()):
            botao = QPushButton(texto_botao)
            botao.setCursor(Qt.PointingHandCursor)
            botao.setMinimumHeight(54)
            botao.setFont(QFont("Segoe UI", 13, QFont.DemiBold))
            botao.setStyleSheet(self._estilo_botao())
            botao.clicked.connect(lambda _checked=False, n=nome: self._selecionar_idioma(n))
            grade.addWidget(botao, 0, i)

        layout_geral.addLayout(grade)
        layout_geral.addStretch()

        rodape = QLabel("Safecomposites3D · Composite Analysis — Vinícius José Martins Coutinho")
        rodape.setAlignment(Qt.AlignCenter)
        rodape.setStyleSheet("color: rgba(255,255,255,150); font-size: 12px; letter-spacing: 1px;")
        layout_geral.addWidget(rodape)

    @staticmethod
    def _estilo_botao():
        return """
            QPushButton {
                background-color: rgba(255, 255, 255, 18);
                border: 1.5px solid rgba(148, 92, 255, 160);
                border-radius: 12px;
                color: #f2f0ff;
                padding: 6px 10px;
            }
            QPushButton:hover {
                background-color: rgba(148, 92, 255, 95);
                border: 1.5px solid #ba8fff;
            }
            QPushButton:pressed {
                background-color: rgba(98, 52, 200, 170);
            }
        """

    # ---------- clique do usuário ----------
    def _selecionar_idioma(self, nome_idioma):
        self.langue = nome_idioma
        self.close()


def main():
    app = QApplication(sys.argv)
    janela = JanelaPrincipal()
    janela.show()
    app.exec()

    langue = janela.langue
    print(langue)
    return langue


def speakit(txt: Path) -> str:
    txt = Path(txt)
    return txt.read_text(encoding="utf-8")


def readkeys() -> str:
    # pasta onde está o script
    pasta_script = Path(__file__).parent
    # caminho do keys.txt
    arquivo = pasta_script / "keys.txt"
    # retorna todo o conteúdo do arquivo como uma string
    return arquivo.read_text(encoding="utf-8")


def save_key(string: str, txt) -> None:
    Path(txt).write_text(string, encoding="utf-8")


def test_language(language: str) -> bool:
    """
    Retorna True se `language` for um dos idiomas aceitos (chave do dicionário IDIOMAS),
    False caso contrário.
    """
    return language in IDIOMAS


def main_our_language():
    keys = readkeys()
    langue = speakit(keys)
    lets_choose = True
    if test_language(langue):
        lets_choose = False
    if lets_choose:
        langue = main()
        save_key(langue, keys)
    return None


# set "True" to call the function only when developing it
if False:
    main_our_language()
