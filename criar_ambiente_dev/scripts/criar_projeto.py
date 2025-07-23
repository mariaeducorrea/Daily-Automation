import os
import subprocess
import shutil


print("Vamos iniciar a criação do projeto...")

project_name = input("Nome do projeto: ")
project_path = input("Local do projeto: ")
version_python = input("Versão python: ")
packages = input("Pacotes a instalar (separados por espaço ou Enter para pular): ")


#Trocando as \ por / para reconhecer o caminho passado 
project_path = project_path.replace("\\", "/")

#Usar os para concatenar caminho passado + nome do projeto que é o diretório criado (BR> full_path = caminho completo)
full_path = os.path.join(project_path, project_name)

#Executar comando terminal para criar projeto com poetry
subprocess.run(["poetry", "new", project_name], cwd=project_path)

subprocess.run(["poetry", "env", "use", f"python{version_python}"], cwd=full_path)

subprocess.run(["poetry", "install"], cwd=full_path)

#Strip remove espaços no começo e final caso tenha e com split deixa somente palavras
if packages.strip():
    print(f"Instalando pacotes {packages.strip()}")
    subprocess.run("poetry add " + packages.strip(), cwd=full_path, shell=True)
else:
    print("Nenhum pacote adicional para instalar.")


if shutil.which("code"):
    subprocess.run("code .", cwd=full_path, shell=True)
else:
    print("VS Code não está disponível no terminal. Pulei essa parte.")


# Impede que o terminal feche imediatamente (opcional)
input("Pressione Enter para sair...")