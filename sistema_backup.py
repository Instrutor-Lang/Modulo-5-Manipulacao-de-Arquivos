import os
import shutil

def fazer_backup(pasta_origem, pasta_destino):
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    for arquivo in os.listdir(pasta_origem):
        origem = os.path.join(pasta_origem, arquivo)
        destino = os.path.join(pasta_destino, arquivo)
        shutil.copy(origem, destino)
        print(f"Copiado: {arquivo}")

fazer_backup("pasta_origem", "pasta_destino")
