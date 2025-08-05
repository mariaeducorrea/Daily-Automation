import os
import subprocess
import shutil


print("Iniciando projeto.")

project_name = input("Nome do projeto: ")
project_path = input("Local do projeto: ")
version_python = input("Versão python: ")
packages = input("Pacotes a instalar (separados por espaço ou Enter para pular): ")


#Trocando as \ por / para reconhecer o caminho passado 
project_path = project_path.replace("\\", "/")

#Usar os para concatenar caminho passado + nome do projeto que é o diretório criado (BR> full_path = caminho completo)
full_path = os.path.join(project_path, project_name)

#Executar comando terminal para criar projeto com poetry / cwd é onde será executado o comando 
subprocess.run(["poetry", "new", project_name], cwd=project_path)

subprocess.run(["poetry", "env", "use", f"python{version_python}"], cwd=full_path)

criando_gitignore = """
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Poetry virtual environments
.venv/

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
*.egg-info/
.installed.cfg
*.egg

# Logs and local config
*.log
*.env
*.ini
*.local
.env.*
.vscode/

# VS Code settings
.vscode/

# macOS
.DS_Store

# Windows
Thumbs.db
ehthumbs.db
"""

with open(os.path.join(full_path, ".gitignore"), "w") as f:
    f.write(criando_gitignore.strip())

#Strip remove espaços no começo e final caso tenha e com split deixa somente palavras
if packages.strip():
    print(f"Instalando pacotes {packages.strip()}")
    subprocess.run("poetry add " + packages.strip(), cwd=full_path, shell=True)
else:
    print("Nenhum pacote adicional para instalar.")


if shutil.which("code"):
    subprocess.run("code .", cwd=full_path, shell=True)
else:
    print("VS Code não está disponível.")


# Impede que o terminal feche imediatamente (opcional)
input("Pressione Enter para sair...")
