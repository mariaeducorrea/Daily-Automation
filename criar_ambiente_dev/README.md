# Criador Automático de Diretórios para Projetos com Python e Poetry

Este script automatiza todo o processo de criação de um novo projeto Python utilizando **Poetry**, já com:

* Criação do diretório do projeto
* Criação do ambiente virtual
* Criação do .gitignore
* Instalação automática de pacotes adicionais (se desejado)
* Abertura do projeto no VS Code (se estiver instalado)

## Objetivo

Facilitar a criação rápida e padronizada de projetos Python, especialmente para:

* Projetos pessoais ou profissionais
* Automação de ambiente de desenvolvimento
* Trabalhos com Poetry e ambientes virtuais

## Bibliotecas e ferramentas utilizadas

| Biblioteca/Ferramenta           | Para que serve?                                                     |
| ------------------------------- | ------------------------------------------------------------------- |
| `os`             | Manipular caminhos e diretórios                                    |
| `subprocess`      | Executar comandos do terminal dentro do script                      |
| `shutil`         | Verificar se o VS Code está disponível no sistema                 |
| `Poetry`         | Gerenciar dependências, ambientes virtuais e estrutura de projetos |
| `VS Code (code)` | (Opcional) Abre o projeto automaticamente após a criação         |

## Como usar o exe

Após criar o exe, é só clicar que irá perguntar:

3. O script vai te perguntar:
   * Nome do projeto
   * Caminho onde deseja criar o projeto
   * Versão do Python desejada (ex: 3.12)
   * Pacotes adicionais (opcional – separados por espaço)
4. Após a execução:
   * O ambiente virtual será criado
   * Os pacotes serão instalados
   * O VS Code será aberto (se estiver disponível)

## Exemplo de entrada

```
Nome do projeto: meu_teste
Local do projeto: C:/Users/SeuNome/Desktop/projetos
Versão python: 3.12
Pacotes a instalar: pandas numpy openpyxl
```

## Como empacotar com PyInstaller (.exe)

Se quiser transformar o script `criar_projeto.py` em um **executável** `.exe`, siga estes passos:

### 1. Instale o PyInstaller (se ainda não tiver)

```
pip install pyinstaller
```

### 2. Gere o executável com o comando:

```
pyinstaller --onefile criar_projeto.py

#ou desta forma para gerar com ico
pyinstaller --onefile --icon=icone_projeto.ico criar_projeto.py

```

### 3. Resultado da geração

Após a execução do comando, será criada a pasta `dist/` dentro do seu diretório atual, e dentro dela estará o arquivo executável `criar_projeto.exe`.

Você pode executar esse arquivo em qualquer computador Windows, sem precisar do Python instalado.

### 4. Limpar arquivos temporários (opcional)

#### No Linux / Git Bash:

```
rm -rf build criar_projeto.spec
```

#### No Windows CMD:

```
rmdir /s /q build
 del criar_projeto.spec
```
