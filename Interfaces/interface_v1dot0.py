# & "C:/Program Files/Python311/python.exe" C:\Users\ucfil\Desktop\desktop\codes\all\FEA\V\inteface-v1.py
import sys
import shutil
import subprocess
from pathlib import Path

# functions that just read txt about language...
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

#geometry 1D
def final_main_v1dot0():
    from Interface_of_Calcul_FRA import main_FRA
    from Interface_of_Calcul_EN import main_ENG
    keys = readkeys()
    langue = speakit(keys)
    langue = langue.lower()

    #french version
    if(langue=="français"):
        main_FRA()
    
    #english version
    if(langue=="english"):
            main_ENG()
    
    #end
    
#"if(True)" only for test...
if(False):

    #here's the main function...
    final_main_v1dot0()
    #
#end